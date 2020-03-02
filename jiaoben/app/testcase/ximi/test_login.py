# coding:utf-8
'''
description:测试小程序
'''
import unittest
from page.ximi.login_page import Login
from page.driver_configure import driver_configure
#from common import slide_handle

import time

class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configur = driver_configure.driver_configure()
        cls.driver = driver_configure.get_driver()
        #cls.GM = slide_handle.gesture_mainpulation()

    def setUp(self):
        self.login_page = Login.login(self.driver)

    def test_login(self):
        self.login_page.login_in("18674669547 ","999999")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
