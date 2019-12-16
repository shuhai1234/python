from po.page.base_page import BasePage

class EditPostPage(BasePage):
    @property
    def title(self):
        return self.by_id('title')

    @property
    def publish_btn(self):
        return self.by_id('publish')

    def set_content(self, content):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" %(content)
        self.js(js)

    def create_post(self, title, content):
        self.title.send_keys(title)
        self.set_content(content)
        self.publish_btn.click()
