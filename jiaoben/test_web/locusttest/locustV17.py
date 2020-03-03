import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import csv
import json
import time

from locust import HttpLocust, TaskSequence, seq_task
import os
import queue
from Common.java_signletom import JavaSingleton
from Common.api_request import locust_report_time, locust_get_workorderId
from locusttest.tools.GetExcelData import get_excel_data
import lxml


# locust参数-保证并发测试数据唯一性，循环取数据.实现调用得到验证码接口
# 通过TaskSequence执行
# 测试从execl 读取测试数据





class MyTaskSet(TaskSequence):

    def on_start(self):
        print("----- Test start -----")
        self.JDClass = JavaSingleton.instance().JDClass
        self.index = 0
        self.user_sessionID = self.user_userID = self.employee_sessionID = self.employee_userID = ""

    def on_stop(self):
        print("----- Test over -----")

    def get_index(self):
        datas = self.locust.share_data[self.index]
        self.index = (self.index + 1) % len(self.locust.share_data)
        print("---执行方法是--------:%s" % (self.index))
        return datas

    def sendreuqest(self,datas,request_data):
        api_type = datas['api_type']
        api_name = datas['api_name']
        method = datas['method']
        url = datas['url']

        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        #参数替换
        if api_type == 'gkeep':
            self.headers = {"User-Agent": "enjoy_link|gkeeper|1.0.0"}
            self.key_3des = "2XHqi0p&jhIrgzKDdTg7B*R3"
            request_data['head']['sessionId'] = self.employee_sessionID
            request_data['head']['userId'] = self.employee_userID
            token = self.JDClass.md5(self.employee_sessionID + self.key_3des + self.employee_userID + str(ttime))
        else:
            self.headers = {"User-Agent": "enjoy_link|ghome|1.0.0"}
            self.key_3des = "J68#*RaGwb*hyC4L1qsS2V%^"
            request_data['head']['sessionId'] = self.user_sessionID
            request_data['head']['userId'] = self.user_userID
            token = self.JDClass.md5(self.user_sessionID + self.key_3des + self.user_userID + str(ttime))
        request_data['head']['token'] = token

        print("加密前:%s"%request_data)

        # dict转成str
        request_data = json.dumps(request_data)

        # 加密请求参数
        request_data = self.JDClass.des3Encode(request_data, self.key_3des)
        #print("加密后:%s"%request_data)

        print("请求url是:%s" % url)

        #发送请求
        r = self.client.post(url,  data=request_data,headers=self.headers)
        #解密参数
        responDecode = self.JDClass.des3Decode(r.text, self.key_3des)

        print("解密返回结果是:%s" % responDecode)

        return json.loads(responDecode) #String 转成dict 返回

    def user_getvalidcode(self):
        try:
            self.user_mobile = self.locust.user_data_queue.get_nowait()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        request_data['mobile'] = ' '.join(self.user_mobile)

        response_data = self.sendreuqest(datas, request_data)
        self.user_validcode = response_data['result']
        self.locust.user_data_queue.put_nowait(self.user_mobile)  # 把取出来的数据重新加入队列

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def user_login(self):#user_login
        datas = self.get_index()

        request_data = json.loads(datas['request_data'])
        request_data['mobile'] = ' '.join(self.user_mobile)
        request_data['content'] = self.user_validcode

        response_data = self.sendreuqest(datas,request_data)
        #得到userid 和 sessionid
        self.user_userID = str(response_data['result']['userId']) # userId 是int, 需在MD5方法中转成string型
        self.user_sessionID = response_data['result']['sessionId']
        self.contactor = response_data['result']['userName']
        self.projectCode = response_data['result']['projectCode']
        self.projectName = response_data['result']['projectName']
        self.houseCode = response_data['result']['mainHouseCode']
        self.buildingCode = response_data['result']['mainBuildingCode']
        self.houseName = response_data['result']['mainHouseName']
        self.buildingName = response_data['result']['mainBuildingName']

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def enjoys_version(self):#  业主端检查版本
        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        request_data['projectCode'] = self.projectCode
        response_data = self.sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def get_user_info(self):#业主信息
        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        response_data = self.sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def save_user_detail(self):
        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        request_data['projectCode'] = self.projectCode
        request_data['projectName'] = self.projectName
        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def query_home_page(self):#APP 首页
        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        request_data['projectCode'] = self.projectCode
        request_data['houseCode'] = self.houseCode
        request_data['buildingCode'] = self.buildingCode
        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def service_three(self):#APP全部服务
        datas = self.get_index()
        response_data = self.sendreuqest(datas, json.loads(datas['request_data']))
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def project_service_list(self):#报事-选择类型
        datas = self.get_index()
        request_data = json.loads(datas['request_data'])
        request_data['projectCode'] = self.projectCode
        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def upload_pic(self):
        datas = self.get_index()
        response_data = {"code": "01", "msg": "图片上传成功！",
                        "result": ["/FOREVER/2019055/6d6e76c305ab408c8be6228c832b62a7.png"]}
        assert '01' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    def reportdata(self,request_data): # 返回报事的数据
        request_data['address'] = self.houseName
        request_data['projectName'] = self.projectName
        request_data['contactor'] = self.contactor
        request_data['reportUserName'] = self.contactor
        request_data['contactMobile'] = ' '.join(self.user_mobile)
        request_data['reportUserMobile'] = ' '.join(self.user_mobile)
        request_data['houseName'] = self.houseName
        request_data['buildingName'] = self.buildingName
        request_data['houseCode'] = self.houseCode
        request_data['buildingCode'] = self.buildingCode

        return request_data


    def reportAdd_immediately(self):#公共报事-公共清洁-立刻报事
        datas = self.get_index()

        request_data = json.loads(datas['request_data'])
        request_data = self.reportdata(request_data)
        report_time_begin  = locust_report_time("reportAdd_immediately", 0)
        request_data['appointmentBeginTime'] = request_data['appointmentEndTime'] = format(report_time_begin)

        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def reportAddr_oneHourAfter(self):#公共报事-公共清洁-下一小时
        datas = self.get_index()

        request_data = json.loads(datas['request_data'])
        request_data = self.reportdata(request_data)
        report_time_begin = locust_report_time("reportAdd_oneHourAfter", 2)
        report_time_end = locust_report_time("reportAdd_oneHourAfter", 3)
        request_data['appointmentBeginTime']  = format(report_time_begin)
        request_data['appointmentEndTime'] = format(report_time_end)

        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def reportAdd_overtime(self):#公共报事-公共清洁-晚上9点后报事
        datas = self.get_index()

        request_data = json.loads(datas['request_data'])
        request_data = self.reportdata(request_data)
        report_time_begin = locust_report_time("reportAdd_overtime", 21)
        report_time_end = locust_report_time("reportAdd_overtime", 23)
        request_data['appointmentBeginTime'] = format(report_time_begin)
        request_data['appointmentEndTime'] = format(report_time_end)

        response_data = self.sendreuqest(datas, request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    def reportforme(self): #首页查看全部工单
        datas = self.get_index()
        response_data = self.sendreuqest(datas, json.loads(datas['request_data']))
        self.workorderId_list = locust_get_workorderId(response_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(1)
    def ienjoys(self):
        self.user_getvalidcode()
        self.user_login()
        self.enjoys_version()
        self.get_user_info()
        self.save_user_detail()
        self.query_home_page()
        self.service_three()
        self.project_service_list()
        self.upload_pic()
        self.reportAdd_immediately()
        self.reportAddr_oneHourAfter()
        self.reportAdd_overtime()
        self.reportforme()

    @seq_task(2)
    def ikeeper(self):
        pass

class MyLocust(HttpLocust):
    """w01~w0100为有效用户名，密码为默认的b123456"""
    task_set = MyTaskSet  # 指向任务集合
    host = "http://10.243.3.49:7080"  # web项目的话这里要设置host属性，否则是报错的

    # 创建队列，先进先出
    user_data_queue = queue.Queue()
    employee_data_queue = queue.Queue()
    try:
        csvHand_u = open("user.csv", "r")
        csvHand_e = open("employee.csv", "r")
        readcsv_u = csv.reader(csvHand_u)
        readcsv_e = csv.reader(csvHand_e)
        try:
            # 把csv中内容存入list 中
            for row in readcsv_u:
                user_data_queue.put_nowait(row)

            for row in readcsv_e:
                employee_data_queue.put_nowait(row)

        except Exception:
            print("list error")
    except Exception:
        print("file error")
    finally:
        # 关闭csv文件
        csvHand_u.close()
        csvHand_e.close()

    # 得到dict  格式的测试数据
    share_data = get_excel_data()

    min_wait = 1000
    max_wait = 3000


if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV17.py")
