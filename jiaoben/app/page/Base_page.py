# coding:utf-8
__author__ = 'Helen'
'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_page:
    def __init__(self, driver):
        self.driver = driver

    # 定义定位属性
    def by_id(self, elem):
         return self.dr.find_element_by_id(elem)

    def by_xpath(self, elem):
         return self.dr.find_element_by_xpath(elem)

    def by_name(self, elem):
        return self.dr.find_element_by_name(elem)

    def find_element(self, *loc):
        ''' 重写find_element方法，显式等待 '''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e