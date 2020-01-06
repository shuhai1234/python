from selenium import webdriver
from time import sleep
import unittest
#from page.login_page import LoginIndexPage
from page.key_page import KeyIndexPage
from case.login import TestLogin



class AssistantCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.driver.implicitly_wait(3)
        print("开始操作")

    @classmethod
    def tearDownClass(cls):
        print("退出")

    def test_key(self):
        driver=self.driver
        TestLogin().login(driver)
        page = KeyIndexPage(driver)
        page.open(self.base_url)
        # 进入到关键词列表
        sleep(3)
        page.Mistress.click()
        sleep(2)
        page.assistant.click()
        sleep(2)
        page.word.click()
        sleep(3)
        page.switch_frame
        sleep(2)
        page.add.click()
        sleep(2)
        page.wordsend.send_keys("s")
        page.save.click()
        sleep(3)
        page.publish.click()
        page.Determine.click()
        sleep(2)




if __name__ == '__main__':
    unittest.main()
    ''''# 构造测试集
    suite.addTest(AssistantCase("test_Scenes"))
    suite.addTest(AssistantCase("test_help"))
    suite.addTest(AssistantCase("test_WakeCase"))
    suite.addTest(AssistantCase("test_key"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)'''
