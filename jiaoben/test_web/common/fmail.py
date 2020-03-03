from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import smtplib

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

    #发送附件
    att = MIMEApplication(open(new_report_fail, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', now + "_report.html"))
    msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(senduser, sendpswd)
    smtp.sendmail(senduser, receuser, msg.as_string())



