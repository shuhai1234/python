from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import yagmail
def  yagmail_send_report(report_file):
    yag = yagmail.SMTP(
        user="1769599174@qq.com",
        password="ptyuklczthifgiic",
        host='smtp.qq.com')
    contents = ['自动化测试邮件']
    yag.send(['507641350@qq.com', '1769599174@qq.com'], 'subject', contents,[report_file])

if __name__ == "__main__":
    test_dir = r'D:\zdh\python\jiaoben\test\case'
    test_report = r'D:\zdh\python\jiaoben\test\report'
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
    yagmail_send_report(yag.send)


# 发送测试报告
'''def send_report(report_file):
    with open(report_file,"rb") as f :
        mail_body =f.read()

    report_name = report_file.split("/")[-1]
    att = MIMEText(mail_body, 'html', 'utf-8')
    att['Content-Type'] = 'text/html'
    att['Content-Disposition'] = 'attachment; filename="'+report_name + '" '
    msgRoot = MIMEMultipart('related')
    msgRoot['Sbuject'] ="自动化测试邮件"
    msgRoot.attach(att)
    smtp = smtplib.STMP()
    smtp.connect(smtp.qq.com)
    smtp.login("1769599174@qq.com","ptyuklczthifgiic")
    smtp.sendmail("1769599174@qq.com",["507641350@qq.com","shuhaiye@126.com"],msgRoot.as_string())
    smtp.quit()
    print("send mail out!!!")'''







