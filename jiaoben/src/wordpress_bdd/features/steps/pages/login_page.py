from base_page import BasePage
from dashboard_page import DashBoardPage

class LoginPage(BasePage):

	@property
	def username(self):
		return self.by_id('user_login')

	@property
	def password(self):
		return self.by_id('user_pass')

	@property
	def login_btn(self):
		return self.by_id('wp-submit')

	def login(self, username, password):
		self.username.send_keys(username)
		self.password.send_keys(password)
		self.login_btn.click()
		return DashBoardPage(self.driver)
