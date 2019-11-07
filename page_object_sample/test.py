'''1、page object 设计模式

* 把元素的定位和操作分开。
dr.search_input.send_keys("page objects")

* 以页面对象的方式维护元素定位

class BaiduIndex():

	def search_input():
		dr.find_element_by_id("kw")

selenium-page-objects 

2、pytest单元测试框架 基本使用

为什么要学pytest ? 更适合做UI自动化

1、整个项目只打开和关闭一次浏览器，减少用例的运行时间。

2、用例失败自动截图, 用例里不需要做任何截图相关的代码。

3、失败重跑，增加用例的稳定性。'''





