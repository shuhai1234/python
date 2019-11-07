from page.base_page import BasePage
from selenium.webdriver.support.select import Select

class LoginIndexPage(BasePage):
    @property
    # 用户名
    def username(self):
        return self.by_id("username")

    @property
    # 密码
    def password(self):
        return self.by_id("password")

    @property
    # 验证码
    def captcha(self):
        return self.by_id("captcha")

    @property
    # 登录
    def button(self):
        return self.by_id("btnLogin")
