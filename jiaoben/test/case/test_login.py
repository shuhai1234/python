# coding:utf-8
from time import sleep
import unittest
from selenium import webdriver
from page.login_page import LoginIndexPage
from common.log import Logger

mylogger = Logger(logger='LoginCase').getlog()


class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.dr.implicitly_wait(3)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def test_login(self):
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        mylogger.info("进入登录页面")
        page.username.send_keys("admin")
        mylogger.info("输入用户名")
        page.password.send_keys("admin123")
        mylogger.info("输入密码")
        page.captcha.send_keys(123)
        mylogger.info("输入验证码")
        page.button.click()

if __name__ == '__main__':
    unittest.main(verbosity=2)
    open= LoginCase()
    open.test_login()







