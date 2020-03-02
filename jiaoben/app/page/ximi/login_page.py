from page.Base_page import Base_page

class Login(Base_page):
    @property
    # 手机号
    def phone(self):
        return self.by_id("com.wld.net:id/login_et_username")

    @property
    # 点击验证码登录
    def Verification_code_login(self):
        return self.by_id("com.wld.net:id/login_tv_photo")

    @property
    # 点击获取验证码
    def Verification_code(self):
        return self.by_id("com.wld.net:id/tv_get_code_button")

    @property
    # 验证码
    def Verification(self):
        return self.by_id("com.wld.net:id/login_auto_code")

    @property
    # 点击登录按钮
    def login(self):
        return  self.by_id("com.wld.net:id/logint_btn")

    def login(self,phone,Verification):
        print (u"请输入手机号",phone)
        self.send_keys(phone)
        print(u"请点击验证码登录")
        self.click(self.Verification_code_login)
        print(u"请点击获取验证码")
        self.click(self.Verification_code)
        print (u"请输入验证码",Verification)
        self.send_keys(self.Verification)
        print (u"请点击登录")
        self.click(self.login)





