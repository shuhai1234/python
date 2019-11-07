import unittest
import os
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import HTMLTestRunner

# 获取测试套件函数
def test_suite(file_path):
    test_unit = unittest.TestSuite()
    # 利用discover获得所有的测试用例，测试用例都是以test_开头
    discover = unittest.defaultTestLoader.discover(file_path, pattern='test_*.py', top_level_dir=None)
    for testsuite in discover:
        for testcase in testsuite:
            test_unit.addTest(testcase)
    return test_unit


# 获取最新的测试结果函数
def newest_report(file_path):
    report_lists = os.listdir(file_path)
    report_lists.sort(key=lambda fn: os.path.getmtime(file_path + fn) if not os.path.isdir(file_path + fn) else 0)
    new_report_dir = os.path.join(file_path, report_lists[-1])
    return new_report_dir


# 发送邮件函数
def send_mail(new_report):
    sender = '1769599174@qq.com'
    receiver = '507641350@qq.com'
    subject = u'测试报告'
    smtpserver = 'smtp.qq.com'
    username = '1769599174@qq.com'  # 和sender相同
    password = 'ptyuklczthifgiic'  # 这里并不是填写qq密码，具体可参考其他文章

    with open(new_report, 'r', encoding='utf-8') as f:
        mail_body = f.read()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header('Tester')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    # 存放测试用例的文件路径，例如下面是我的路径
    test_path = "D:\\zdh\\test\\case\\"
    # 测试报告所在目录
    test_report = 'D:\\zdh\\test\\report\\'
    tests = test_suite(test_path)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_report + now + '_result.html'
    print("测试报告生成地址：%s" % filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title="ui自动化测试测试报告",
                                           description="用例执行情况")
    runner.run(tests)
    fp.close()
    new_report = newest_report(test_path)
    send_mail(new_report)

