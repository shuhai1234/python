from appium import webdriver
from selenium.webdriver.common.by import By
from poium import Page, PageElement, PageElements
import Basepage

driver = webdriver.Remote("http://localhost:4723/wb/hub",Basepage.Base.caps)

#class Loginpage(Page):
#定位元素方式
        #@property
        #def username_input(self):
                #return self.by_id("login_et_username")

        #@property
        #def password_input(self):
                #return self.by_id("login_pass_word")

       # @property
        #def login_button(self):
                #return self.by_id("logint_btn")

class Basepage(Page):
         username_input = PageElement(id_="login_et_username", describe="用户名输入框")
         password_input = PageElement(id_="login_pass_word", describe="验证码输入框")
         login_button = PageElement(id_="logint_btn", describe='登录')

         def username(self, username):
             name = self.driver.find_element_by_id(self.username_input)
             name.send_keys(username)  # 输入用户名

         def password(self, password):
             pwd = self.driver.find_element_by_id(self.password_input)
             pwd.send_keys(password)  # 输入验证码

         def button(self,button):
             but=self.driver.find_element_by_id(self.login_button)
             but.click()   #点击登录按钮









