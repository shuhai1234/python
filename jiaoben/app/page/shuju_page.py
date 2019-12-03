from page.Base_page import Base_page
class ShujuIndexPage(Base_page.Base):
    @property
    # 点开小程序
    def xiaochenxu(self):
        return self.by_id("com.tencent.mm:id/zs")

    @property
    # 点击今日收款top 中的”更多“按钮
    def more(self):
        return self.by_xpath("//*[@text='更多']")

    @property
    # 进入到分析页面
    def analysis(self):
        return self.by_xpath("//*[@text='分析']")

























    








