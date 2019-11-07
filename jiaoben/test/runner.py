import unittest
import time
import HTMLTestRunner
from common.fmail import *

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new


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

    #②搜索最新生成的文件
    new_report = new_report(test_report)
    #③发送邮件
    send_mail(new_report, filename1, now)

    # 展示测试报告html
    #driver = webdriver.chrome()
    #driver.get("D:/zdh/test/report/" + now +"_result.html")

    stoptime = time.strftime('%H:%M:%S')
    print("结束时间为：%s" %stoptime)