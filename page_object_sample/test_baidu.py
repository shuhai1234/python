import unittest
from time import sleep
from selenium import webdriver
from new_baidu_page import BaiduIndexPage
from page_objects import PageWait, PageSelect
from loger import MyLogger

#mylogger = MyLogger(logger='testlogger').put_logger()

# 在用例里面，看不到任何元素的定位
class BaiduSearch(unittest.TestCase):
    """ 使用parameterized进行百度搜索参数化"""

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    @unittest.skip("跳过")
    def test_search_case(self):
        """ 搜索关键字 page objects"""
        page = BaiduIndexPage(self.dr)
        page.get(self.base_url)

        PageWait(page.search_input)   # 相当于显示等待
        page.search_input.send_keys("page objects")
        page.search_button.click()
        sleep(2)
        result = page.search_result
        for r in result:
            print(r.text)

    def test_search_setting(self):
        """ 搜索关键字 page objects"""
        page = BaiduIndexPage(self.dr)
        page.get(self.base_url)
        page.move_to_element(page.settings)
        page.search_setting.click()
        PageWait(page.select_number)
        PageSelect(page.select_number, value="20")





if __name__ == '__main__':
    unittest.main(verbosity=2)


