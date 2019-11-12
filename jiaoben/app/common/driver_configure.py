# coding:utf-8
import pytest
from appium import webdriver
@pytest.fixture(scope='session')
def driver():
    caps = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "3e515f8",
        "appPackage": "com.tencent.mm",
        "appActivity": ".ui.LauncherUI",
        'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "autoLaunch": False
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()









