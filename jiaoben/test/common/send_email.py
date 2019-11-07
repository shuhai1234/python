#conding:utf8
import os
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# ******************定义发送邮件******************
def send_mail(file_new):
    f = open(file_new, 'rb')
    filename = f.read()
    f.close()
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    sender = '1769599174@qq.com'
    receiver = '507641350@qq.com'
    username = '1769599174@qq.com'
    password = 'ptyuklczthifgiic'
    smtp.login(username, password)

    subject = '附件为最新测试报告，望查收'
    msg = MIMEText(filename, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'Shu<1769599174@qq.com>'
    msg['To'] = '507641350@qq.com'
    #print(msg)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    print('email has send out!')


# ===========================查找测试报告目录，找到最新的测试报告文件 ===========================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new


# 判断元素是否存在
    def is_element_exist(self, css):
        s = self.driver.find_element_by_css(css_selector=css)
        if len(s) == 0:
            print("元素未找到：%s" % css)
            return False
        elif len(s) == 1:
            return True
        else:
            print("找到%s个元素：%s" % (len(s), css))
            return False







