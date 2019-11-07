from selenium import webdriver
from time import sleep
import unittest
from page.key_page import KeyIndexPage
from page.login_page import LoginIndexPage

class KeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.dr.implicitly_wait(1)

    def test_Login(self):
        # 登录
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        sleep(2)
        page.username.send_keys("admin")
        page.password.send_keys("admin123")
        page.captcha.send_keys(123)
        page.button.click()

    def test_key(self):
        # 进入到关键词列表
        page = KeyIndexPage(self.dr)
        sleep(3)
        page.Mistress.click()
        sleep(3)
        page.assistant.click()
        sleep(3)
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
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)







