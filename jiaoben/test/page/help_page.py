from page.base_page import BasePage


class HelpIndexPage(BasePage):
    @property
    # 小蜜
    def Mistress(self):
        return self.by_id("menu_773")

    @property
    # 个人语音助手
    def assistant(self):
        return self.by_xpath("//*[@id='menu_1003']")

    @property
    # 帮助中心
    def help(self):
        return self.by_xpath("//*[@id='menu_1008']")

    @property
    def switch_frame(self):

        loc = self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/iframe")
        self.dr.switch_to_frame(loc)
        #layui - layer - shade1

    @property
    # 新增
    def add(self):
        return self.by_xpath("//*[@id='btn_add']")

    '''def switch_frame1(self):
        loc = self.by_xpath("//div[@class='layui-layer-content']/iframe")
        self.dr.switch_to_frame(loc)'''

    @property
    def switch_frame1(self):
        loc = self.by_xpath("//*[@class='layui-layer-content']/iframe")
        self.dr.switch_to.frame(loc)

    @property
    # 进入到配置页面
    def peizhi(self):
        return self.by_xpath("//*[@id='name']")

    @property
    def key(self):
        return self.by_xpath("/html/body/div/form/div[2]/div/div[1]/input")

    @property
    # 保存
    def sava(self):
        return self.by_xpath("//*[@id='btnSave']")

    #文件上传




