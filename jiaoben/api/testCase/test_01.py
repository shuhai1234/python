import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel


url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
log_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'log')

@paramunittest.parametrized(*log_xls)
class TestUser(unittest.TestCase):
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

    def checkResult(self):  # 断言
        url1 = "https://mapi.58wld.com/weleadin-web-mapi"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))    #   将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)   # 将响应转换为字典格式
        print(ss)
       #if self.case_name == 'queryByContent':   # 如果case_name是queryByContent，说明合法，返回的code应该为200
            #self.assertEqual(ss['code'], 200)


if __name__ == '__main__':
    unittest.main()



