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
from locusttest.tools.GetExcelData import get_excel_data

# locust参数-保证并发测试数据唯一性，循环取数据.实现调用得到验证码接口
#可以顺序执行
#测试从execl 读取测试数据
#重构了send_request方法之前

class MyTaskSet(TaskSequence):

    def on_start(self):
        print("----- Test start -----")
        # self.run_username()  # 执行task前运行一次run_sql函数
        self.JDClass = JavaSingleton.instance().JDClass
        self.headers = {"User-Agent": "enjoy_link|gkeeper|1.0.0"}
        self.key_3des = "2XHqi0p&jhIrgzKDdTg7B*R3"
        self.sessionID = ""
        self.userID = ""

        self.index = 0

    def on_stop(self):
        print("----- Test over -----")

    def replace_variable(self,api_type,apy_name,url,method,request_data):

        request_data = eval(request_data)

        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        token = self.JDClass.md5(self.sessionID + self.key_3des + self.userID + str(ttime))
        request_data['head']['token'] = token
        request_data['head']['sessionId'] = self.sessionID
        request_data['head']['userId'] = self.userID
        request_data['mobile'] = ' '.join(self.mobile)

        if apy_name == 'login':
            request_data['content'] = self.validcode



        # dict转成str
        request_data = json.dumps(request_data)
        print("加密前:%s"%request_data)

        # 加密请求参数
        request_data = self.JDClass.des3Encode(request_data, self.key_3des)
        print("加密后:%s"%request_data)

        print("请求url是:%s" % url)

        #发送请求
        r = self.client.post(url,  data=request_data,headers=self.headers)
        #解密参数
        responDecode = self.JDClass.des3Decode(r.text, self.key_3des)

        print("解密返回结果是:%s" % responDecode)

        return json.loads(responDecode) #String 转成dict 返回


    def sendreuqest(self,datas):


        api_type = datas['api_type']
        api_name = datas['api_name']
        method = datas['method']
        url = datas['url']
        request_data = json.loads(datas['request_data'])


        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        token = self.JDClass.md5(self.sessionID + self.key_3des + self.userID + str(ttime))
        request_data['head']['token'] = token
        request_data['head']['sessionId'] = self.sessionID
        request_data['head']['userId'] = self.userID
        request_data['mobile'] = ' '.join(self.mobile)

        if api_name == 'login':
            request_data['content'] = self.validcode



        # dict转成str
        request_data = json.dumps(request_data)
        print("加密前:%s"%request_data)

        # 加密请求参数
        request_data = self.JDClass.des3Encode(request_data, self.key_3des)
        print("加密后:%s"%request_data)

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
        print("当前下标是:%s" % self.index)
        #self.client.get(url)
        return datas



    @seq_task(1)

    def get_valid_code(self):
        print("------------1111111111111------------------")
        try:
            self.mobile = self.locust.user_data_queue.get_nowait()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)


        """
        datas = self.test_visit()
        url = datas['url']
        request_data = datas['request_data']
        api_type = datas['api_type']
        api_name = datas['api_name']
        method = datas['method']
        response_data = self.replace_variable(api_type, api_name, url, method, request_data)
        """

        datas = self.test_visit()
        response_data = self.sendreuqest(datas)

        self.validcode = response_data['result']


        self.locust.user_data_queue.put_nowait(self.mobile)  # 把取出来的数据重新加入队列


        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)



    @seq_task(2)
    def login_ghome(self):
        print("------------*******222222222222222*******------------------")

        datas = self.test_visit()
        url = datas['url']
        request_data = datas['request_data']
        api_type = datas['api_type']
        api_name= datas['api_name']
        method= datas['method']

        response_data = self.replace_variable(api_type, api_name, url, method, request_data)

        self.userID = str(response_data['result']['userId']) # userId 是int, 需在MD5方法中转成string型
        self.sessionID = response_data['result']['sessionId']



        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

    @seq_task(3)
    def check_version(self):
        print("------------333333333333------------------")

        datas = self.test_visit()
        url = datas['url']
        request_data = datas['request_data']
        api_type = datas['api_type']
        api_name= datas['api_name']
        method= datas['method']
        response_data = self.replace_variable(api_type, api_name, url, method, request_data)

        assert '10000' in json.dumps(response_data), "Respense error: " + json.dumps(response_data)

class MyLocust(HttpLocust):
    """w01~w0100为有效用户名，密码为默认的b123456"""
    task_set = MyTaskSet  # 指向任务集合
    host = "http://10.243.3.49:7080"  # web项目的话这里要设置host属性，否则是报错的
    user_data_queue = queue.Queue()  # 创建队列，先进先出

    try:
        csvHand = open("user.csv", "r")
        readcsv = csv.reader(csvHand)
        try:
            # 把csv中内容存入list 中
            for row in readcsv:
                user_data_queue.put_nowait(row)
        except Exception:
            print("list error")
    except Exception:
        print("file error")
    finally:
        # 关闭csv文件
        csvHand.close()
    # 得到dict  格式的测试数据
    share_data  = get_excel_data()


    min_wait = 1000
    max_wait = 3000


if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV14.py")