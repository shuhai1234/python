from selenium import webdriver
from time import sleep
import unittest
from page.help_page import HelpIndexPage
from page.login_page import LoginIndexPage
#from ddt import ddt,data,file_data,unpack


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
        sleep(2)

    def test_help(self):
        page = HelpIndexPage(self.dr)
        page.Mistress.click()
        sleep(2)
        page.assistant.click()
        sleep(2)
        page.help.click()
        sleep(2)
        page.switch_frame
        sleep(2)
        page.add.click()
        sleep(3)
        page.switch_frame1
        sleep(3)
        page.peizhi.send_keys("广告")
        sleep(2)
        page.key.send_keys("1234")
        sleep(2)
        page.sava.click()
        sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)




