import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        url1 = "http://wldoperation.58wld.com/go.php/Index/shopRed"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        login = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(login)  # 将响应转换为字典格式
        print (ss)
        if self.case_name == 'info':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'info_error':# 同上
            self.assertEqual(ss['code'], 1001)
        if self.case_name == 'info_null':# 同上
            self.assertEqual(ss['code'], 1001)

if __name__ == '__main__':
    unittest.main(verbosity=2),


