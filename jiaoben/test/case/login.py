#from selenium import webdriver
from page.login_page import LoginIndexPage
import time

class TestLogin():
    def login(self,driver):
        time.sleep(3)
        page = LoginIndexPage(driver)
        page.username.send_keys("admin")
        page.password.send_keys("admin123")
        page.captcha.send_keys(123)
        page.button.click()
        time.sleep(3)
        return driver














