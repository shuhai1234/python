from selenium import webdriver
from common.Log import Logger
from common import dirconfig
import threading

localReadConfig = dirconfig.ReadConfig()


import threading




class Driver:

    def __init__(self):
        self.log = Logger.get_log()
        self.logger = self.log.get_logger()

        self.browser = webdriver.Chrome()

    def open_browser(self, name1, name2):
        """
        Do something for browser
        :return: browser
        """
        self.logger.info("Open browser")

        # 窗口最大化
        self.browser.maximize_window()

        # 打开地址链接
        url = localReadConfig.get_webServer(name1, name2)
        self.browser.get(url)
        return self.browser

    def close_browser(self):
        """
        quit browser
        :return:
        """
        self.browser.quit()
        self.logger.info("Quit browser")

    def get_driver(self):
        """
        get web driver
        :return:
        """
        return self.browser


class MyDriver:

    driver = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_browser():

        if MyDriver.driver is None:
            MyDriver.mutex.acquire()
            MyDriver.driver = Driver()
            MyDriver.mutex.release()

        return MyDriver.driver

if __name__ == "__main__":
    driver = MyDriver.browser()
    browser = driver.open_browser()