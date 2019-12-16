#coding: utf-8
import unittest
from selenium import webdriver # selenium1 rc | selenium2 = webdriver + rc | selenium3
from selenium.webdriver.common.action_chains import ActionChains
import time
from page.login_page import LoginPage
from page.dashboard_page import DashboardPage
from config.data import TEST_DATA

class LoginCase(unittest.TestCase):

    def setUp(self): #每个用例执行之前执行
        self.dr = webdriver.Chrome()

    def tearDown(self):
        self.dr.quit()

    def test_login_success(self):
        username = TEST_DATA['username']
        password = TEST_DATA['password']

        login_page = LoginPage(self.dr, 'wp-login.php')
        dashboard_page = login_page.login(username, password)

        self.assertTrue('wp-admin' in self.dr.current_url)
        self.assertTrue(username in dashboard_page.greeting_link.text)
