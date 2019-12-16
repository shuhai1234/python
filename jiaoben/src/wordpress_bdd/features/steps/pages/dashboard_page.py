from base_page import BasePage

class DashBoardPage(BasePage):

	@property
	def greeking_link(self):
		return self.by_css('#wp-admin-bar-my-account .ab-item')

	@property
	def greeking_link_text(self):
		return self.greeking_link.text
