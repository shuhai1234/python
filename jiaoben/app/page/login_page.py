'''页面;登录页面'''


from common import Base_page
from appium.webdriver.common import mobileby

class Login_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 手机输入框
    user = (by.ID, "com.ansiyida.cgjl:id/editText_phone")
    # 密码输入框
    password = (by.ID, "com.ansiyida.cgjl:id/editText_password")
    # 登录按钮
    enter_button = (by.ID, "com.ansiyida.cgjl:id/btn_login")

    # 输入手机号码
    def input_user(self, username):
        self.send_keys(username, *self.user)
    # 输入密码
    def input_password(self,pwd):
        self.send_keys(pwd, *self.password)
    # 点击登录按钮
    def click_enter_button(self):
        self.find_element(*self.enter_button).click()
    # 点击注册按钮
    def click_register_button(self):
        self.find_element(*self.register_button).click()
    # 点击qq按钮
    def click_qq_button(self):
        self.find_element(self.qq_button).click()
    # 点击微信按钮
    def click_wechat_button(self):
        self.find_element(self.wechat_button).click()
    # 点击微博按钮
    def click_microblog_button(self):
        self.find_element(self.microblog_button).click()
