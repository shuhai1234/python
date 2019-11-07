from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
'''
description:手势操作
'''
class SlideHandle():
    def __init__(self, driver):
        self.driver = driver

class gesture_mainpulation:
    def swipeUp(driver, t=500, n=1):
        '''向上滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(driver, t=500, n=1):
        '''向下滑动屏幕'''
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


    # 允许弹框
    def always_allow(self, driver, number=5):
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    # 封装toast判断
    def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False



