from page_objects import PageObject, PageElement, PageElements
from common import Base_page
from appium.webdriver.common import mobileby

class Shuju_page(Base_page.Base_page):
    xiaochenxu = PageElements(id_="com.tencent.mm:id/zs"[0], describe="小程序")
    more = PageElement(xpath="//*[@text='更多']", describe="更多按钮")
    analysis = PageElement(xpath="//*[@text='分析']", describe="分析")
    seemore = PageElement(xpath="//*[@text='查看更多']", describe="查看更多")

    income = PageElement(xpath="//*[@text='收益']", describe="收益")
    me = PageElement(xpath="//*[@text='我的']", describe="我的")
    Unbind = PageElement(xpath="//*[@text='解除绑定']", describe="解除绑定")
    Unbound = PageElement(xpath="//*[@text='未绑定']", describe="未绑定")
    phone = PageElement(xpath="//*[@text='请输入手机号']", describe="手机号")
    Verificationcode = PageElement(xpath="//*[@text='验证码']", describe="验证码")







    








