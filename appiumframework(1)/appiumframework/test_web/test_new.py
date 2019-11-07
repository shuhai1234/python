
import  unittest
from selenium import webdriver
import time
from ddt import ddt,data
class Baidusearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Firefox()
        cls.base_url = "https//www.baidu.com"


    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def daidu_search(self,search_key):
        self.dr.find_element_by_id("kw").send_keys("search_key")
        self.dr.find_element

     #参数化
    @data("python","selenium""untttse")
    def test_search(self, search_key):
            dr = self.dr
            dr.get(self.base_url)
            self.dr.daidu_search("search_key")
            self.assertEqual(dr.title,search_key + "百度搜索")

    if __name__ == "__main__":
                unittest.main()
