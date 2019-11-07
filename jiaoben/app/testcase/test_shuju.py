# coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from common.slide_handle import gesture_mainpulation

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0.1',
                'deviceName': '3e515f8',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Appium',
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
                }


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

# 向下滑动
gesture_mainpulation.swipeDown(driver)

# 点开小程序
driver.find_elements_by_id("com.tencent.mm:id/zs")[0].click()
time.sleep(4)

print(driver.contexts)
time.sleep(5)

# 向上滑动
gesture_mainpulation.swipeUp(driver)

# 点击今日收款top 中的”更多“按钮
driver.find_element_by_xpath("//*[@text='更多']").click()
time.sleep(5)
driver.tap([(32, 61), (168, 107)], 500)

# 进入到分析页面
driver.find_element_by_xpath("//*[@text='分析']").click()
time.sleep(3)
gesture_mainpulation.swipeUp(driver)

# 点击近30天签约商家中的“查看更多”按钮
driver.find_element_by_xpath("//*[@text='查看更多']").click()
gesture_mainpulation.swipeUp(driver)
driver.tap([(32, 61), (168, 107)], 500)

gesture_mainpulation.swipeUp(driver)

# 切换到收益列表
driver.find_element_by_xpath("//*[@text='收益']").click()
time.sleep(3)
gesture_mainpulation.swipeUp(driver)

# 点击近30天收益处的“查看更多”按钮
driver.find_element_by_xpath("//*[@text='查看更多']").click()
gesture_mainpulation.swipeUp(driver)
driver.tap([(32, 61), (168, 107)], 500)

# 进入我的
driver.find_element_by_xpath("//*[@text='我的']").click()
time.sleep(3)

# 点击“切换为小蜜商家 ”
driver.find_element_by_xpath("//*[@text='切换为小蜜商家']").click()
time.sleep(3)

# 进入到实时
driver.find_element("//*[@text='实时']").click()
gesture_mainpulation.swipeUp(driver)
gesture_mainpulation.swipeDown(driver)
# 点击今日顾客明细“更多“按钮”
driver.find_element_by_xpath("//*[@text='更多']").click()
driver.tap([(32, 61), (168, 107)], 500)

# 进入到分析
driver.find_element_by_xpath("//*[@text='分析']").click()
sel = driver.tap([(540, 242), (702, 294)], 500)
sel.click()
driver.find_element_by_xpath("//*[@text='近30天']").click()

# 进入我的
driver.find_element_by_xpath("//*[@text='我的']").click()





















