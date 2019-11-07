
import HTMLTestRunner
import unittest
import time
import  pdfkit

from common.send_email import *

if __name__ == "__main__":
    test_dir = r'D:\zdh\test\case'
    test_report = r'D:\zdh\test\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 1
    filename1 = test_report + '\\' + now + 'result.html'
    fp = open(filename1, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title="ui自动化测试测试报告",
                                           description="用例执行情况")
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    print(new_report)
    send_mail(new_report)  # 发送测试包