import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import csv
import json
import time,datetime

from locust import task, TaskSet, HttpLocust, TaskSequence, seq_task
import pymysql
import os
import queue
from Common.java_signletom import JavaSingleton

# locust参数-保证并发测试数据唯一性，循环取数据.实现调用得到验证码接口
#可以顺序执行

class MyTaskSet(TaskSequence):

    def on_start(self):
        print("----- Test start -----")
        # self.run_username()  # 执行task前运行一次run_sql函数
        self.JDClass = JavaSingleton.instance().JDClass
        self.headers = {"User-Agent": "enjoy_link|gkeeper|1.0.0"}
        self.key_3des = "2XHqi0p&jhIrgzKDdTg7B*R3"
        self.sessionID = ""
        self.userID = ""

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

        # dict转成str
        request_data = json.dumps(request_data)
        print("加密前")
        print(request_data)
        # 加密请求参数
        request_data = self.JDClass.des3Encode(request_data, self.key_3des)
        print("加密后")
        print(request_data)

        #发送请求
        r = self.client.post(url,  data=request_data,headers=self.headers)
        #解密参数
        responDecode = self.JDClass.des3Decode(r.text, self.key_3des)

        return responDecode



    @seq_task(1)
    def get_valid_code(self):
        path = "/enjoylink/code/getValidCode.do"
        try:
            self.mobile = self.locust.user_data_queue.get_nowait()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

        request_data = '{"mobile":"18565693063","head":{"deviceInfo":"NEM-AL10|6.0[1.0.1]","sessionId":"","timestamp":1558426012022,"token":"995bf81e07284f30861737440c5cff17","userId":""}}'

        request_data = eval(request_data)

        ttime = int(round(time.time() * 1000))
        request_data['head']['timestamp'] = ttime

        token = self.JDClass.md5(self.sessionID + self.key_3des + self.userID + str(ttime))
        request_data['head']['token'] = token
        request_data['head']['sessionId'] = self.sessionID
        request_data['head']['userId'] = self.userID
        request_data['mobile'] = ' '.join(self.mobile)



        # dict转成str
        request_data = json.dumps(request_data)

        #加密请求参数
        request_data = self.JDClass.des3Encode(request_data, self.key_3des)


        r = self.client.post(path,  data=request_data,headers=self.headers)

        responDecode = self.JDClass.des3Decode(r.text, self.key_3des)


        self.locust.user_data_queue.put_nowait(self.mobile)  # 把取出来的数据重新加入队列

    @seq_task(3)
    def check_version(self, pwd="a111111"):
        print("------------333333------------------")
        print(self.mobile)
        path = "/portal/3333333333.do"
        self.client.get(path, headers=self.headers)

    @seq_task(2)
    def login_ghome(self):
        print("------------2222222222------------------")
        url = "/enjoylink/ghome/user/loginGhome.do"
        request_data = '{"mobileVersion":"NEM-AL10|6.0","mobileOs":"01","appVersion":"1.0.0","content":"9999","channel":"home","head":{"timestamp":1558947449923,"macId":"","deviceInfo":"NEM-AL10|6.0[1.0.0]home","token":"c373d326db099121cbc589e0a6d8d04e"},"mobile":"18565693063"}'

        response_data = self.replace_variable("ghome", "login", url, "post", request_data)
        print("解密返回结果是:")
        print(response_data)


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



    min_wait = 1000
    max_wait = 3000


if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV13.py")