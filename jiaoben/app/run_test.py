# coding=utf-8
import unittest
import time
import HTMLTestRunner
from common import send_mail
from config.globalparameter import test_case_path, report_name
# 构建测试集，包含testcase目录下所有发test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*_.py')
# 执行测试
if __name__ == "__main__":
    report = report_name+"Report.html"
    fp = open(report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="UI自动化测试报告",
        description="用例执行情况"
    )

runner.run(suite)
fp.close()
# 发送邮件
time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
email = send_mail.send_email()
email.sendReport()

if __name__ == "__main__":
    unittest.main()


