# coding:utf-8
from time import sleep
import unittest
from selenium import webdriver
from page.login_page import LoginIndexPage
from common.log import Logger
from parameterized import parameterized
import time

#mylogger = Logger(logger='LoginCase').getlog()

class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.dr.implicitly_wait(3)
        # 从表文件中读数据,teatdata.txt文件需要存在
        '''with open("./teatdata.txt", "r") as f:
            data = f.readlines()
        cls.test_data = []
        for d in data:
            cls.test_data.append(d.strip("\n"))'''
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
    #参数化
    @parameterized.expand([
        ("case01","admin","admin123","123")
       # ("case02","admin","admin123","12345")
    ])

    def test_login(self,name,username,password,captcha):
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        #mylogger.info("进入登录页面")
        page.username.send_keys(username)
        #page.username.send_keys(self.test_data[0])  # 从文件中读取数据
        #mylogger.info("输入用户名")
        page.password.send_keys(password)
        #mylogger.info("输入密码")
        page.captcha.send_keys(captcha)
        #mylogger.info("输入验证码")
        page.button.click()
        time.sleep(3)
       # title = LoginIndexPage.title

if __name__ == '__main__':
    unittest.main(verbosity=2)
    #open= LoginCase()






