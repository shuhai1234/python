import os
import win32com.client as win32
import datetime
import readConfig
import getpathInfo
from common.Log import logger

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import smtplib

'''read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径'''
logger = logger

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new

def send_mail(new_report,new_report_fail,now):
    '''
    :param new_report:获取最新的文件
    :param new_report_fail:获取最新的文件的路径
    :param now:当前生成报告的时间
    :return:
    '''

    senduser = '1769599174@qq.com'
    sendpswd = 'ptyuklczthifgiic'
    receuser = '507641350@qq.com'
#获取报告文件：'related'43行
    f = open(new_report, 'rb')
    body_main = f.read()

    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = senduser
    msg['To'] = receuser
    #邮件内容
    text = MIMEText(body_main, 'html', 'utf-8')
    msg.attach(text)
    # 发送附件
    att = MIMEApplication(open(new_report_fail, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', now + "_report.html"))
    msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(senduser, sendpswd)
    smtp.sendmail(senduser, receuser, msg.as_string())


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




