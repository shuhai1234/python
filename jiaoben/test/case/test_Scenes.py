from selenium import webdriver
from time import sleep
import unittest
from page.Scenes_page import ScenesIndexPage
from page.login_page import LoginIndexPage

class ScenesCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.base_url = "http://admin.58wld.com/wldadmin.php/login"
        cls.dr.implicitly_wait(1)
        print(cls.dr.current_url)  # 当前url

    def test_Login(self):
        # 登录
        page = LoginIndexPage(self.dr)
        page.open(self.base_url)
        sleep(2)
        page.username.send_keys("admin")
        page.password.send_keys("admin123")
        page.captcha.send_keys(123)
        page.button.click()

    # 进入到小蜜-个人语音助手—场景列表
    def test_Scenes(self):
        page = ScenesIndexPage(self.dr)
        # 进入到小蜜-个人语音助手—场景列表
        page.Mistress.click()
        sleep(2)
        page.assistant.click()
        sleep(2)
        page.clasification.click()
        sleep(2)
        # 增加场景
        page.switch_frame
        sleep(2)
        page.added.click()
        sleep(3)
        page.switch_frame1
        sleep(2)
        page.clasificati
        sleep(2)
        page.clasificati1
        sleep(2)
        page.Key
        sleep(2)
        page.add.click()
        sleep(2)
        page.operation
        sleep(2)
        page.template.send_keys("345")
        sleep(2)
        page.role.click()
        page.role1.click()
        sleep(2)
        page.save.click()


    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)











































dr.quit()  # 退出