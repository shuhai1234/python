import requests
import unittest
class jiqiren(unittest.TestCase):
    def setUp(self):
        print("-----------开始测试-----------")
    def tearDown(self):
        print("--------------测试结束---------------")
    # 根据内容查询场景信息
    def test_queryByContent(self):
        self.new_url = "https://mapi.58wld.com/weleadin-web-mapi/robot/queryByContent.do"
        self.data = {"ucode": "100201809281045605043941670912", "content": "二维码"}
        res = requests.post(self.new_url, json=self.data)
        result = res.json()
        print(result)
# 查询机器人功能是否开启
    def test_open(self):
        self.url = "https://mapi.58wld.com/weleadin-web-mapi/robot/isOpen.do"
        res1 = requests.post(self.url)
        result1 = res1.json()
        print(result1)
# 获取唤醒语信息
    def test_RouseRemind(self):
        self.url = "https://mapi.58wld.com/weleadin-web-mapi/robot/queryRouseRemind.do"
        res2 = requests.post(self.url)
        result2 = res2.json()
        print(result2)
# 获取技能配置信息
    def test_SkillConfig(self):
        self.url = "https://mapi.58wld.com/weleadin-web-mapi/robot/querySkillConfig.do"
        res3 = requests.post(self.url)
        result3 = res3.json()
        print(result3)
# 刷新关键字
    def test_reloadKeyWord(self):
        self.url = "https://mapi.58wld.com/weleadin-web-mapi/robot/reloadKeyWord.do"
        res4 = requests.post(self.url)
        result4 = res4.json()
        print(result4)

if __name__ == '__main__':
        # test_data.init_data()  # 初始化接口测试数据
    unittest.main()







