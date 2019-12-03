# coding:utf-8
'''
description:测试小程序
'''
import unittest
from page.shuju_page import ShujuIndexPage
from page.driver_configure import *
from common import slide_handle
import time

class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = slide_handle.gesture_mainpulation()


    def test_01(self):
        self.page = ShujuIndexPage(self.driver)
        self.page .xiaochenxu.click()
        time.sleep(3)
        self.GM.swipeDown(self.driver)
        time.sleep(3)

    def test_02(self):
        self.page = ShujuIndexPage(self.driver)
        # 点击今日收款列表中的“更多”按钮
        self.page.more.click()
        time.sleep(3)
        # 返回到首页（原生页面的）
        self.driver.tap([(32, 61), (168, 107)], 500)
        # 点击分析
        self.shuju_page.click_analysis_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()