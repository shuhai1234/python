from locust import HttpLocust, TaskSet, task
import os

class WebsiteTasks(TaskSet):
    def on_start(self):
        print("----- Test start -----")

    def on_stop(self):
        print("----- Test over -----")

    def login(self):
        self.loginUrl = "/pro/user-login.html"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

        data = {"account": "shuhaiye", "pwd": "Wld123456"}
        r = self.client.post(self.loginUrl, data=data, headers=self.headers)

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
            assert "产品页" in r.text


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://192.168.1.32:82"
    min_wait = 1000
    max_wait = 5000

if __name__ == '__main__':
        # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locustV21.py --host=http://192.168.1.32:82")


