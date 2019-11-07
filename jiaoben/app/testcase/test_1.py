# coding:utf-8
'''
description:测试小程序
'''
import unittest
from page import shuju_page
from common import slide_handle
from common import driver_configure
import time


class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = slide_handle.gesture_mainpulation()


    def test_01login(self):
        '''打开小程序页面'''
        # 向下滑动
        self.shuju_page = shuju_page.Shuju_page(self.driver)
        time.sleep(3)
        self.GM.swipeDown(self.driver)
        time.sleep(3)
        # 点击“数据领地”小程序
        self.shuju_page.click_xiaochenxu_button()
        self.time.sleep(3)
        print(self.driver.contexts)
        time.sleep(3)
        # 向上滑动
        self.GM.swipeUp(self.driver)

        # 点击今日收款列表中的“更多”按钮
        self.shuju_page.click_more_button()
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
