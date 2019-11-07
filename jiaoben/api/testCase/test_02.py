#!/usr/bin/python
# coding=utf-8
import requests
import unittest

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class DemoApi(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def queryByContent(self, ucode, content):
        """
        登录接口
        :param ucode: 商家
        :param content: 备注
        """
        url = urljoin(self.base_url, 'login')
        data = {
            'ucode': ucode,
            'content': content
        }

        return requests.post(url, data=data).json()



class TestQueryByContent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'https://mapi.58wld.com/weleadin-web-mapi/robot/queryByContent.do'
        cls.ucode = '100201809281045605043941670912'
        cls.content = '二维码'
        cls.app = DemoApi(cls.base_url)

    def test_queryByContent(self):
        """
        测试登录
        """
        response = self.app.queryByContent(self.ucode, self.content)
        assert response['code'] == 200
        assert response['msg'] == 'success'

if __name__ == '__main__':
    unittest.main()