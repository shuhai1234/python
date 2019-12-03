# coding=utf-8
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    '''蝗虫行为类'''

    def on_start(self):
        print("-------------开始测试------------")

    def on_stop(self):
        print("-------------结束测试------------")

    def hears(self):
        h = {
            "Content-Type": "application/x-www-form-urlencoded",
            "appVersion": "v4.1.0",
            "channelId": "1",
            "osVersion": "",
            "termTyp": "web",
        }


#令牌
    def queryTokenInfo(self):
        # host = ' mapi.58wld.com/weleadin-web-mapi'  # 服务器地
        loginUrl ="/order/queryTokenInfo.do"
        body = {"tokenId": "20190812112053389002508578240337e"}
        r = self.client.post(loginUrl, data=body, headers=self.hears.h)
        print(r.text)
        #assert "parent.location='/pro/index.html'" in r.text

    # 获取商户信息
    @task(2)
    def userDatum(self):
        print("---获取商户信息---")
        loginUrl = "/userDatum/getUserInfo.do"
        body = {"cUcode": "100201809281045605043941670912"}
        r = self.client.post(loginUrl, data=body, headers=self.hears.h)
        print(r.text)
        #assert "parent.location='/pro/index.html'" in r.text

    # 线下扫码下单支付
    @task(1)
    def order(self):
        print("---线下扫码下单支付---")
        loginUrl = "/order/createOffLineOrder.do"
        body = {
            "payType": "WXPAY",
            "amount": "0.1",
            "scanType": "SCAN",
            "merchantId": "100201809281045605043941670912",
            "openId": "oARqGxIliMI5Pa3gOEVdMJaBi87k",
            "source": "WECHAT"
        }
        r = self.client.post(loginUrl, data=body, headers=self.hears.h)
        print(r.text)
        #assert "parent.location='/pro/index.html'" in r.text

    # 通过openid获取用户信息
    @task(1)
    def user_authBind(self):
        print("---通过openid获取用户信息---")
        loginUrl = "/user/authBind.do"
        body = {
            "cUnionid": "oKlI5v8j2b44qx8Gn07fBvAriOJk",
            "cType": "1",
            "cOpenid": "oARqGxIliMI5Pa3gOEVdMJaBi87k"
                }
        r = self.client.post(loginUrl, data=body, headers=self.hears.h)
        print(r.text)
        #assert "parent.location='/pro/index.html'" in r.text



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 1000

if __name__ == "__main__":
    import os
    os.system("locust -f locustV19.py --host=http://mapi.58wld.com/weleadin-web-mapi")
