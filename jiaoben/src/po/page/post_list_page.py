from page.base_page import BasePage

class PostListPage(BasePage):
    @property
    def first_post(self):
        return self.by_css('.row-title')
