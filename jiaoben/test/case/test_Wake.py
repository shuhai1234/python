from selenium import webdriver
from time import sleep
import unittest
from page.wake_page import WakeIndexPage
from page.login_page import LoginIndexPage


class ScenesCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.dr.implicitly_wait(1)

    def test_login(self):
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        sleep(2)
        page.username.send_keys("admin")
        page.password.send_keys("admin123")
        page.captcha.send_keys(123)
        page.button.click()
        sleep(3)

    def test_wake(self):
        # 进入到唤醒提示
        page = WakeIndexPage(self.dr)
        sleep(3)
        page.Mistress.click()
        sleep(3)
        page.assistant.click()
        sleep(3)
        page.wake.click()
        sleep(3)
        page.switch_frame
        sleep(2)
        page.add.click()
        sleep(2)
        page.configuration.send_keys("哈1")
        page.save.click()
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


