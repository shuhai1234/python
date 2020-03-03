from page.base_page import BasePage
from time import sleep
class KeyIndexPage(BasePage):
    @property
    # 小蜜
    def Mistress(self):
        return self.by_id("menu_773")
        sleep(3)

    @property
    # 个人语音助手
    def assistant(self):
        return self.by_xpath("//*[@id='menu_1003']")
        sleep(3)

    @property
    # 关键词列表
    def word(self):
        return self.by_id("menu_1006")
        sleep(3)

        # 重写switch_frame方法

    @property
    def switch_frame(self):
        loc = self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/iframe")
        self.dr.switch_to_frame(loc)


    @property
    # 新增
    def add(self):
        return self.by_xpath("//*[@id='btn_add']")
    @property
    # 关键词
    def wordsend(self):
        return self.by_id("keyword")
    @property
        # 保存
    def save(self):
        return self.by_xpath("/html/body/div[3]/div[3]/a[1]")
    @property
    # 发布
    def publish(self):
        return self.by_id("btn_publish")
    @property
    # 确定
    def Determine(self):
        return self.by_xpath("/html/body/div[3]/div[3]/a[1]")






