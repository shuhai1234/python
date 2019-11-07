import unittest
import requests
import json
import sys
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
sys.path.append("../..")  # 提升2级到项目根目录下


class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserLogin")   #读取TestUserReg工作簿的所有数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_login_password_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        #print(res)
        #print(res.text)
        #print(expect_res)
        self.assertEqual(res.text, expect_res)  # 断言

    def test_queryByContent(self):
        case_data = get_test_data(self.data_list, 'test_queryByContent')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')   # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
        log_case_info('test_queryByContent', url, data, expect_res, res.text)
        # print("res1==>", res.text)   #打印
        # print("expect_res2==>", expect_res)
        # print("res.text==>", res.text[26:-1])
        a = json.loads(res.text)  #
        b = json.loads(expect_res)
        #print("111=>>", type(a.get("code")))
        #print("222==>", type(b.get("code")))
        self.assertEqual(a.get("code"), b.get("code"))  # 断言

    def test_open(self):
        case_data = get_test_data(self.data_list, 'test_open')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')   # excel中的标题也必须是小写url
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url)  # 表单请求，数据转为字典格式
        log_case_info('test_open', url, expect_res, res, res.text)
        #self.assertEqual(res.text, expect_res)  # 断

    @classmethod
    def setDownClass(cls):
        print("-------------------测试结束----------------------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
