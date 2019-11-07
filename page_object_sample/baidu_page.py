
class BasePage():

	def __init__(self, driver):
		self.dr = driver	

	def open(self, url):
		self.dr.get(url)

	def by_id(self, elem):
		return self.dr.find_element_by_id(elem)


class BaiduIndexPage(BasePage):

	# 搜索框 
	@property	
	def search_input(self):
		return self.by_id("kw")

	# 搜索按钮
	@property
	def search_button(self):
		return self.by_id("su")


class MailLoginPage(BasePage):
	pass




"""
import time 


class A:

	@property
	def get_time(self):
		return time.ctime()

a = A()
c = a.get_time

print(c)
"""