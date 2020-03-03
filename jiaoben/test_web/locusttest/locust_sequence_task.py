from locust import TaskSet, task, HttpLocust, TaskSequence, seq_task
import os

#https://blog.csdn.net/qq_36255988/article/details/82627133
#https://www.cnblogs.com/changqing8023/p/10204951.html
#https://www.cnblogs.com/monogem/p/10715637.html
class WebUser(TaskSet):
    @task(5)
    def first_task(self):
        print('执行5次；')

    @task(2)
    class IosUser(TaskSet):
        @task(1)
        def second_task(self):
            print('1次')

        @task(2)
        def three_task(self):
            print('2次')
            self.interrupt()

    @task(2)
    class AndroidUser(TaskSequence):
        @seq_task(2)
        @task(1)
        def android_task(self):
            print('这是android用户；')
            self.interrupt()

        @seq_task(1)
        @task(1)
        def ios_task(self):
            print('这是ios用户；')


class LocustFun(HttpLocust):
    host = 'https://passport.cnblogs.com'
    task_set = WebUser
    max_wait = 6000
    min_wait = 3000


if __name__ == '__main__':
    os.system("locust -f locustV5.py")
