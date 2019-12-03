import os
import re
import sys


from Common.api_request import report_time, get_workorderId

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


import csv
import json
import time

from locust import HttpLocust, TaskSequence, seq_task
import os
import queue
from Common.java_signletom import JavaSingleton
from locusttest.tools.GetExcelData import get_excel_data

# locust参数-保证并发测试数据唯一性，循环取数据.实现调用得到验证码接口
#可以顺序执行 TaskSequence
#测试从execl 读取测试数据




class MyTaskSet(TaskSequence):

    def on_start(self):
        print("----- Test start -----")

        self.JDClass = JavaSingleton.instance().JDClass
        self.index = 0
        self.sessionID = self.userID =self.employee_sessionID = self.employee_userID=""
        """"
        self.userID = ""
        self.employee_sessionID = ""
        self.employee_userID = ""
        """

    def on_stop(self):
        print("----- Test over -----")

    def sendreuqest(self,datas):

        api_type = datas['api_type']
        api_name = datas['api_name']
        method = datas['method']
        url = datas['url']
        request_data = json.loads(datas['request_data'])

        if api_type == 'gkeep':
            self.headers = {"User-Agent": "enjoy_link|gkeeper|1.0.0"}
            self.key_3des = "2XHqi0p&jhIrgzKDdTg7B*R3"
        else:
            self.headers = {"User-Agent": "enjoy_link|ghome|1.0.0"}
            self.key_3des = "J68#*RaGwb*hyC4L1qsS2V%^"


        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        token = self.JDClass.md5(self.sessionID + self.key_3des + self.userID + str(ttime))
        request_data['head']['token'] = token
        request_data['head']['sessionId'] = self.sessionID
        request_data['head']['userId'] = self.userID
        if api_name == 'login' or api_name == 'getValidCode':
            request_data['mobile'] = ' '.join(self.mobile)

        if api_name == 'login':
            request_data['content'] = self.validcode
        if api_name in ["checkVersion","saveUserDetail" ,"queryHomePage","serviceThree","projectServiceList","upload"]:
            request_data['projectCode'] = self.projectCode
        if api_name == 'saveUserDetail':
            request_data['projectName'] = self.projectName
            #request_data['projectCode'] = self.projectCode
            #request_data['clientId'] = self.clientId #暂时找不到
        if api_name == 'queryHomePage':
            #request_data['projectCode'] = self.projectCode
            request_data['houseCode'] = self.houseCode
            request_data['buildingCode'] = self.buildingCode

        if api_name == 'reportAdd_immediately':
            request_data['address'] = self.houseName
            request_data['projectName'] = self.projectName

            request_data['contactor'] = self.contactor
            request_data['reportUserName'] = self.contactor
            request_data['contactMobile'] = self.mobile
            request_data['reportUserMobile'] = self.mobile
            request_data['houseName'] = self.houseName
            request_data['buildingName'] = self.buildingName
            request_data['houseCode'] = self.houseCode
            request_data['buildingCode'] = self.buildingCode

        api_method = re.search(r'[^/]+$', url).group(0)  # 得到请求方法
        #指定报事时间
        if api_method == 'reportAdd.do':
            if api_name == 'reportAdd_immediately': #立刻报事
                report_time_begin = report_time(api_method,api_name,0)
                report_time_end = report_time(api_method,api_name,0)
            elif api_name == 'reportAdd_oneHourAfter':  # 下一小时
                report_time_begin = report_time(api_method,api_name,2)
                report_time_end = report_time(api_method,api_name,3)
            else:  # 晚上9点后报事
                report_time_begin = report_time(api_method,api_name,21)
                report_time_end = report_time(api_method,api_name,22)

            request_data['appointmentBeginTime'] = format(report_time_begin)
            request_data['appointmentEndTime'] = format(report_time_end)

        # dict转成str
        request_data = json.dumps(request_data)
        print("加密前:%s" % request_data)
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


    def employee_sendreuqest(self,datas,request_data):

        api_type = datas['api_type']
        api_name = datas['api_name']
        method = datas['method']
        url = datas['url']

        #参数替换
        if api_type == 'gkeep':
            self.headers = {"User-Agent": "enjoy_link|gkeeper|1.0.0"}
            self.key_3des = "2XHqi0p&jhIrgzKDdTg7B*R3"
            request_data['head']['sessionId'] = self.employee_sessionID
            request_data['head']['userId'] = self.employee_userID
        else:
            self.headers = {"User-Agent": "enjoy_link|ghome|1.0.0"}
            self.key_3des = "J68#*RaGwb*hyC4L1qsS2V%^"
            request_data['head']['sessionId'] = self.sessionID
            request_data['head']['userId'] = self.userID


        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        token = self.JDClass.md5(self.sessionID + self.key_3des + self.userID + str(ttime))
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

    def test_visit(self):
        datas = self.locust.share_data[self.index]

        self.index = (self.index + 1) % len(self.locust.share_data)
        print("---执行方法是--------:%s" %(self.index))

        return datas

    @seq_task(1)
    def getvalidcode(self):
        #print("---执行方法是:--------%s"%(self.index+1))
        try:
            self.mobile = self.locust.user_data_queue.get_nowait()
            print("--------------mobile is :" % self.mobile)
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

        response_data = self.sendreuqest(self.test_visit())

        self.validcode = response_data['result']
        self.locust.user_data_queue.put_nowait(self.mobile)  # 把取出来的数据重新加入队列

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    @seq_task(2)
    def loginghome(self):

        response_data = self.sendreuqest(self.test_visit())

        self.userID = str(response_data['result']['userId']) # userId 是int, 需在MD5方法中转成string型
        self.sessionID = response_data['result']['sessionId']
        self.contactor = response_data['result']['userName']
        self.projectCode = response_data['result']['projectCode']
        self.projectName = response_data['result']['projectName']
        self.houseCode = response_data['result']['mainHouseCode']
        self.buildingCode = response_data['result']['mainBuildingCode']
        self.houseName = response_data['result']['mainHouseName']
        self.buildingName = response_data['result']['mainBuildingName']

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(3)
    def checkversion(self):
        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(4)
    def getuserinfo(self):
        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)
    @seq_task(5)
    def saveuserdetail(self):

        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(6)
    def queryhomepage(self):

        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(7)
    def servicethree(self):

        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(8)
    def projectservicelist(self):

        response_data = self.sendreuqest(self.test_visit())

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(9)
    def uploadPic(self):
        self.test_visit()
        response_data = {"code": "01", "msg": "图片上传成功！",
                        "result": ["/FOREVER/2019055/6d6e76c305ab408c8be6228c832b62a7.png"]}
        assert '01' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(10)
    def reportAdd_immediately(self):
        response_data = self.sendreuqest(self.test_visit())
        assert '请求执行成功！' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(11)
    def reportAddr_oneHourAfter(self):
        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(12)
    def reportAdd_overtime(self):
        response_data = self.sendreuqest(self.test_visit())
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(13)
    def reportforme(self): #首页查看全部工单
        response_data = self.sendreuqest(self.test_visit())
        self.workorderId_list = get_workorderId(response_data)
        print(self.workorderId_list)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    @seq_task(14)
    def employee_getvalidcode(self):#employee_getValidCode
        try:
            self.employee_mobile = self.locust.employee_data_queue.get_nowait()
            self.employee_mobile = ' '.join(self.employee_mobile)
            print(self.employee_mobile)
        except queue.Empty:
            print('employee account data run out, test ended.')
            exit(0)

        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])

        request_data['mobile'] = ' '.join(self.employee_mobile)

        response_data = self.employee_sendreuqest(datas, request_data)
        self.employee_validcode = response_data['result']
        self.locust.employee_data_queue.put_nowait(self.employee_mobile)  # 把取出来的数据重新加入队列

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(15)
    def employee_login(self):#employee_login

        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        request_data['mobile'] = ' '.join(self.employee_mobile)
        request_data['content'] = self.employee_validcode

        response_data = self.employee_sendreuqest(datas,request_data)
        #得到userid 和 sessionid
        self.employee_userID = str(response_data['result']['userId']) # userId 是int, 需在MD5方法中转成string型
        self.employee_sessionID = response_data['result']['sessionId']

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    @seq_task(16)
    def welcomepage_employee(self):#welcomepage_employee

        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        request_data['employeeId'] = self.employee_userID

        response_data = self.employee_sendreuqest(datas,request_data)

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(17)
    def userdetail(self):#员工信息

        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])

        response_data = self.employee_sendreuqest(datas,request_data)

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    @seq_task(18)
    def register_areaAndSkillQuery(self):#地区与技能

        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])

        response_data = self.employee_sendreuqest(datas,request_data)

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(19)
    def workclock(self):#workClock
        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        response_data = self.employee_sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(20)
    def workStatusUpdate(self):#技能签入
        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        response_data = self.employee_sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


    @seq_task(21)
    def signAreaAndSkillQuery(self):#技能签入成功
        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        response_data = self.employee_sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(22)
    def workOrderList(self):#查看全部工单
        datas = self.test_visit()
        request_data = json.loads(datas['request_data'])
        request_data['userId'] = self.employee_userID

        response_data = self.employee_sendreuqest(datas,request_data)
        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)


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

    """
    employee_data_queue = queue.Queue()  # 创建队列，先进先出
    try:
        csvHand = open("employee.csv", "r")
        readcsv = csv.reader(csvHand)
        try:
            # 把csv中内容存入list 中
            for row in readcsv:
                employee_data_queue.put_nowait(row)
                print("employee is %s"%row)
        except Exception:
            print("list error")
    except Exception:
        print("file error")
    finally:
        # 关闭csv文件
        csvHand.close()
    """
    # 得到dict  格式的测试数据
    share_data  = get_excel_data()


    min_wait = 1000
    max_wait = 3000


if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV15.py")
