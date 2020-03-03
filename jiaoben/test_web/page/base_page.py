from selenium.webdriver.support.select import Select
class BasePage():
    def __init__(self, driver):
        self.dr = driver
# 定义打开浏览器
    def open(self, url):
        self.dr.get(url)
# 定义定位属性
    def by_id(self, elem):
        return self.dr.find_element_by_id(elem)

    def by_xpath(self, elem):
        return self.dr.find_element_by_xpath(elem)

    def by_name(self,elem):
        return self.dr.find_element_by_name(elem)

# 定位时间控件
    def shijia(self):
         js = '$(\'input[id=startEffectiveDate]\').removeAttr(\'readonly\')'
         self.driver.execute_script(js)
         js_value = self.driver.find_element_by_id("startEffectiveDate")
         js_value.send_keys("2019-01-13")
# 滚动条
    #回到顶部
    def scroll_top(self):
        if self.driver.name == "chrome":
          js = "var q=document.body.scrollTop=0"
        else:
          js = "var q=document.documentElement.scrollTop=0"
          return self.driver.execute_script(js)

    def scroll_foot(self):
       # 拉到底部
        if self.driver.name == "chrome":
           js = "var q=document.body.scrollTop=10000"
        else:
             js = "var q=document.documentElement.scrollTop=10000"
             return self.driver.execute_script(js)

    # select下拉框
    def sel(self):
        Select(self.by_xpath("//*[@id='app_type']")).select_by_value('0')

    # 警告框
    def alert(self):
        alert = self.driver.switch_to.alert
    # 获得警告框提示信息
        alert_text = alert.text
        print(alert_text)
    # 接受警告框
        alert.accept()







