from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from parameterized import parameterized
caps = {
            'platformName': 'Android',
            'deviceName': 'b8df22a17d53',  # 可有可无
            'platformVersion': '6.0.1',
            "android_uiautomator": "uiautomator2",
            # apk包名
            'appPackage': 'com.wld.proxy',
            # apk的launcherActivity
            'appActivity': 'com.wld.module_proxy.main.ProxyLoadAct',
            # 如果存在activity之间的切换可以用这个
            'unicodeKeyboard': "True",
            # 隐藏手机中的软键盘
            'resetKeyboard': "True"
        }
driver = webdriver.Remote("http://127.0.0.1:4723/wb/hub",caps)

def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
    swipLeft(driver,n=3)

sleep(10)


def login(self, username, password):
    name=self.driver.find_element_by_id("login_et_username").send_keys("username")
    self.driver.find_element_by_id("com.wld.proxy:id/login_pass_word").send_keys("password")
    self.driver.find_element_by_id("com.wld.proxy:id/logint_btn").click()
    sleep(2)


# 参数化
@parameterized.expand([
     ("case1", "13975823812", "111111"),
     #("case2", "13428967050", "111111")
])

def test_login(self,username,password):

#driver.find_element_by_xpath("//*[@text='立即体验']")
    self.driver.find_element_by_id("login_et_username").send_keys("username")
    self.driver.find_element_by_id("com.wld.proxy:id/login_pass_word").send_keys("password")
    self.driver.find_element_by_id("com.wld.proxy:id/logint_btn").click()
    sleep(5)

def always_allow(driver, number=5):
        for i in range(number):
                loc = ("xpath", "//*[@text='允许']")
                try:
                        e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                        e.click()
                except:
                        pass
if __name__ == "__main__":
    # 调用始终允许函数
    always_allow(driver)










