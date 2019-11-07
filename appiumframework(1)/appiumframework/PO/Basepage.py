from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
'''
class Base():
   driver = None
    caps = {
            'platformName': 'Android',
            'deviceName': 'b8df22a17d53',  # 可有可无
            'platformVersion': '6.0.1',
            "android_uiautomator": "uiautomator2",
            # apk包名
            'appPackage': 'com.wld.proxy',
            # apk的launcherActivity
            'appActivity': 'com.wld.module_proxy.main.ProxyLoadAct',
            # 如果存在activity之间的切换可以用这个
            'unicodeKeyboard': True,
            # 隐藏手机中的软键盘
            'resetKeyboard': True
        }

    def __init__(self, appium_driver):
        self.driver = appium_driver'''

#封装id
    #def by_id(self, elem):
            #self.dr.find_element_by_id(elem)
class MyTest(unittest.TestCase):
    # 允许弹框
    def always_allow(driver, number=5):
            for i in range(number):
                loc = ("xpath", "//*[@text='允许']")
                try:
                    e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                    e.click()
                except:
                    pass

    def swipeUp(driver, t=500, n=1):
        ''' 向上滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(driver, t=500, n=1):
        ''' 向下滑动屏幕 '''
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(driver, t=500, n=1):
        '''向左滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    def swipRight(driver, t=500, n=1):
        '''向右滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)




