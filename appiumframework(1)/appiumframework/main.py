# coding=utf-8
import unittest
import time
import HTMLTestRunner
import os
curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, ".\\report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, ".\\testcase")
def add_case(casepath=case_path, rule="test_*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '.\\report\\.' + now + 'result.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="UI自动化测试报告",
                                               description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)

