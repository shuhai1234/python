# coding=utf-8
from locust import HttpLocust, TaskSet, task, seq_task
import queue
import csv
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from locusttest.tools.GetExcelData import get_excel_data
'''
实现场景：先登录（只登录一次），然后访问->我的地盘页->产品页->项目页
访问我的地盘页面权重为2，产品页和项目页权重各为1
'''
class MyTaskSet(TaskSet):

    def on_start(self):
        print("----- Test start -----")

    def on_stop(self):
        print("----- Test over -----")

    def login(self, pwd="Wld123456"):
        self.headers = {
            "Origin": "http://192.168.1.32:82",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        loginUrl = "/pro/user-login.html"

        try:
            user_data = self.locust.queue_data.get()  # 从队列中取出user赋值给user_data
            print(user_data)
        except queue.Empty:
            print("数据为空了...")
            exit()
        data = {"account": user_data, "pwd": pwd}
        r = self.client.post(loginUrl, data=data, headers=self.headers)
        print(r.text)
        assert "parent.location='/pro/index.html'" in r.text
    # 任务1-我的地盘
    @task(2)
    def pro_my(self):
        print("---访问页面-我的地盘---")
        r = self.client.get("/pro/my/")
        assert "我的地盘" in r.text
    # 任务2-产品页
    @task(1)
    def pro_product(self):
        print("---访问页面-产品页---")
        r = self.client.get("/pro/product-browse.html/")
        assert "需求列表" in r.text

    # 任务3-项目
    @task(1)
    def pro_prject(self):
        print("---访问页面-项目---")
        r = self.client.get("/pro/project/")
        assert "项目首页" in r.text
# 排序执行
    @seq_task(1)
    def ienjoys(self):
        self.pro_my()
        self.pro_prject()
        self.pro_product()

    @seq_task(2)
    def ikeeper(self):
        pass
class MyLocust(HttpLocust):
    """w01~w0100为有效用户名，密码为默认的Wld123456"""
    task_set = MyTaskSet  # 指向任务集合
    host = "http://192.168.1.32:82"  # web项目的话这里要设置host属性，否则是报错的

    # 创建队列，先进先出
    '''user_data_queue = queue.Queue()
    data_queue = queue.Queue()    # 实例化一个队列
    try:
        csvHand_u = open("user.csv", "r")
        csvHand_e = open("employee.csv", "r")
        readcsv_u = csv.reader(csvHand_u)
        readcsv_e = csv.reader(csvHand_e)
        try:
           #把csv中内容存入list 中
            for row in readcsv_u:
                user_data_queue.put_nowait(row)   #把每一个user存到队列中

            for row in readcsv_e:
                data_queue.put_nowait(row)     #把每一个user存到队列中

        except Exception:
            print("list error")
    except Exception:
        print("file error")
    finally:
        # 关闭csv文件
        csvHand_u.close()
        csvHand_e.close()'''


    user_data_queue = queue.Queue()
    queue_data = queue.Queue()  # 实例化一个队列
    for i in range(1, 101):
        user = "w0" + str(i)
        print(user)
        queue_data.put_nowait(user)  # 把每一个user存到队列中

    # 得到dict  格式的测试数据
    share_data = get_excel_data()
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV18.py --host=http://192.168.1.32:82")





