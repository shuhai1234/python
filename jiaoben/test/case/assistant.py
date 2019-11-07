from selenium import webdriver
from time import sleep
import unittest
from page.login_page import LoginIndexPage
from page.key_page import KeyIndexPage
from case.test_login import LoginCase


class AssistantCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始操作")
        #cls.dr = webdriver.Chrome()
        #cls.dr.maximize_window()
        #cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        #cls.dr.implicitly_wait(1)
        #cls.LoginCase.test_login()

    '''def test_login(self):
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        sleep(2)
        page.username.send_keys("admin")
        page.password.send_keys("admin123")
        page.captcha.send_keys(123)
        page.button.click()'''

    def test_key(self):
        # 进入到关键词列表
        LoginCase.test_login()
        page = KeyIndexPage(self.dr)
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

    @classmethod
    def tearDownClass(cls):
        print("退出")


if __name__ == '__main__':
    unittest.main()
    ''''# 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(AssistantCase("test_login"))
    suite.addTest(AssistantCase("test_Scenes"))
    suite.addTest(AssistantCase("test_help"))
    suite.addTest(AssistantCase("test_WakeCase"))
    suite.addTest(AssistantCase("test_key"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)'''
