from locust import HttpLocust, TaskSet, task
import os

class UserBehavior(TaskSet):

    def on_start(self):
        print("-------------开始测试------------")

    def on_stop(self):
        print("-------------结束测试------------")

    @task(1)  # ----装饰器，默认值为1，权重越大执行频率越高
    def baidu(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):  # 设置性能测试
    task_set = UserBehavior  # 指向一个定义了的用户行为类
    min_wait = 3000  # 用户执行任务之间等待时间的下界，
    max_wait = 6000  # 用户执行任务之间等待时间的上界，

if __name__ == "__main__":
    os.system("locust -f locustV20.py --host=https://www.baidu.com")

    from lxml import etree

    tree = etree.parse('文件名')
    res = tree.xpath('// li[ @class ="item-0"]')
    print(res)