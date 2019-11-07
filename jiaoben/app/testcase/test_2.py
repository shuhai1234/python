import unittest
from ddt import data, ddt, unpack
from page import login_page
from common import driver_configure
from config.globalparameter import img_name
from common import slide_handle



@ddt
class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = driver_configure.Driver_Config()
        cls.driver = driver.get_driver()
        cls.Gm = slide_handle.gesture_mainpulation
    def test_01(self):
        self.login_page = login_page.Login_page(self.driver)
        self.login_page.click_enter_button()
        self.Gm.swipe_down(self.driver)
        self.login_page.click_enter_button()



    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
