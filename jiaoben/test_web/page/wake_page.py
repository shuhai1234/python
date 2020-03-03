from page.base_page import BasePage


class WakeIndexPage(BasePage):
    @property
    # 小蜜
    def Mistress(self):
        return self.by_id("menu_773")

    @property
    # 个人语音助手
    def assistant(self):
        return self.by_xpath("//*[@id='menu_1003']")

    @property
    def wake(self):
        return self.by_xpath("//*[@id='menu_1007']")

    @property
    def switch_frame(self):
        loc = self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/iframe")
        self.dr.switch_to_frame(loc)

    @property
    # 新增
    def add(self):
        return self.by_xpath("//*[@id='btn_add']")

    @property
        #配置信息
    def configuration(self):
        return self.by_xpath("//*[@id='keyword']")

    @property
    # 保存
    def save(self):
        return self.by_xpath("/html/body/div[3]/div[3]/a[1]")







