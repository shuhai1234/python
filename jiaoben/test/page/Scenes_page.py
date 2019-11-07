
#from page_objects import PageObject, PageElement
from page.base_page import BasePage
from selenium.webdriver.support.select import Select

class ScenesIndexPage(BasePage):

    @property
    # 小蜜
    def Mistress(self):
        return self.by_id("menu_773")

    @property
    # 个人语音助手
    def assistant(self):
        return self.by_xpath("//*[@id='menu_1003']")

    @property
    # 场景列表
    def clasification(self):
        return self.by_id("menu_1004")

    @property
    # 新增
    def added(self):
        return self.by_xpath("/html/body/div/div[2]/div/div/div[2]/form/a")

    # 重写switch_frame方法
    @property
    def switch_frame(self):
        loc = self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/iframe")
        self.dr.switch_to_frame(loc)

    @property
    def switch_frame1(self):
        loc = self.by_xpath("//*[@class='layui-layer-content']/iframe")
        self.dr.switch_to.frame(loc)

    @property
    # 场景分类
    def clasificati(self):
        Select(self.by_xpath("//*[@id='app_type']")).select_by_value('0')

    @property
    def clasificati1(self):
        Select(self.by_xpath("//*[@id='scenario_category_id']")).select_by_value('6')


    @property
    def Key(self):
        return Select(self.by_xpath("//*[@id='choice_keywords']")).select_by_value('234')


    @property
    # 添加
    def add(self):
        return self.by_xpath("//*[@id='choice_keywords_add']")

    @property
    # 执行对应的操作
    def operation(self):
        Select(self.by_xpath("//*[@id='skip_type']")).select_by_value('0')


    @property
    # 添加模板
    def template(self):
        return self.by_xpath("//*[@id='template']")

    @property
    # 角色
    def role(self):
        return self.by_xpath("/html/body/div/div/div/div/div[2]/form/div[11]/div/label[1]/input")

    @property
    def role1(self):
        return self.by_xpath("/html/body/div/div/div/div/div[2]/form/div[11]/div/label[2]/input")

    @property
    # 保存
    def save(self):
        return self.by_xpath("//*[@id='btn-add']")












