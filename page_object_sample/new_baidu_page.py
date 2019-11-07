from page_objects import PageObject, PageElement, PageElements


class BaiduIndexPage(PageObject):
	search_input = PageElement(id_="kw", timeout=3, describe="输入框")
	search_button = PageElement(css="#su", timeout=20, describe="按钮")
	# 定位一组元素
	search_result = PageElements(xpath="//div/h3/a")

	settings = PageElement(link_text="设置")
	search_setting = PageElement(css=".setpref", describe="搜索设置")
	select_number = PageElement(id_="nr", describe="选择每页显示个数")

