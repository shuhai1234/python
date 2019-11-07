import  unittest
from selenium import webdriver
import time
from parameterized import parameterized
class Baidusearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https//www.baidu.com"


    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def Baidu_search(self,search_key):
        self.dr.find_element_by_id("kw").send_keys("search_key")
        self.dr.find_element_by_id("su").click()
        time.sleep(2)
  #参数化
    #@parameterized.expand([
        #("case1","selenium","selenium_百度搜索"),
        #("case2","python","python_百度搜索")
    #])

    def test_search(self):
        dr = self.dr
        dr.get(self.base_url)
        self.dr.Baidu_search("selenium")
        self.assertEqual(dr.title == "assert_title")

      #实现跳过
        @unittest.skip("跳过")
        def test_search_python(self):
            dr = self.dr
            dr.get(self.base_url)
            dr.daidu_search("python")
            self.assertEqual(dr.title == "python_百度搜索")


if __name__ == "__main__":
    unittest.main()

