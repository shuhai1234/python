import time
from appium import webdriver
import unittest
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
sys.path.append("..")
from PO import Basepage
class ShujuTest(unittest.TestCase):
    def setUp(self):
        print("从这里开始执行")
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0.1',
                'deviceName': '3e515f8',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Appium',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)

    def test_swipeDown(self):
        Basepage.MyTest(self.driver)
    time.sleep(2)



























    def tearDown(self):
        print("从这里结束")


