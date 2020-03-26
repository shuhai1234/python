import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from common.configEmail import *
import time
import common.Log


path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = common.Log.logger

class AllTest:#定义一个类AllTest
    def __init__(self):#初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, "report.html")  # result/report.html
        self.caseListFile = os.path.join(path, "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []
        log.info('resultPath'+resultPath)  # 将resultPath的值输入到日志，方便定位查看问题
        log.info('caseListFile'+self.caseListFile)  # 同理
        log.info('caseList'+str(self.caseList))  # 同理

if __name__ == "__main__":
    test_dir = r'E:\interfaceTest\testCase'
    test_report = r'E:\interfaceTest\result'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename1 = test_report + '\\' + now + 'result.html'
    fp = open(filename1, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title="接口自动化测试测试报告",
                                           description="用例执行情况")
    runner.run(discover)
    fp.close()

    # ②搜索最新生成的文件
    new_report = new_report(test_report)
    # ③发送邮件
    send_mail(new_report, filename1, now)

    # 展示测试报告html
    #driver = webdriver.chrome()
    #driver.get("D:/zdh/test/report/" + now +"_result.html")

    stoptime = time.strftime('%H:%M:%S')
    print("结束时间为：%s" %stoptime)






