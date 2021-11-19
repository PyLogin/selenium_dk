# -*- coding: UTF-8 -*-

import time
import unittest
import HTMLTestRunner
import sys
import os
import requests
import ExSendEmail

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

PATH = "F://Pycharm//autocase_dk//src"
REPORT_PATH = "F://Pycharm//autocase_dk//result//"

def sendemail(receiver,file_name):
    tmp = str(upload_result(file_name))
    mail_body = '<p><a href = ' + tmp + '>' + tmp + '</a></p>'
    f = open(file_name, 'rb')
    mail_body += f.read()
    f.close()
    ExSendEmail.SendMail(receiver, "贷款自动化结果", mail_body)

def upload_result(file_name):
    url = 'http://10.142.71.235/se_auto_report/uploadreport.php'
    report_file_name = file_name.split('/')
    files = {'file': (report_file_name[-1], open(file_name, 'rb'))}
    req = requests.post(url, files=files)
    return req.text

def suit():
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(PATH, pattern='dk_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            print 'adding test...' + str(test_suite)
            test_unit.addTests(test_case)
            print(test_unit)
    return test_unit



if __name__ == "__main__":
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)


    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    filename = REPORT_PATH + now + "_result.html"
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'贷款自动化Case',
        description=u'用例执行情况：')

    runner.run(suit())
    fp.close()
    receivers = ['supengyue@sogou-inc.com']
    sendemail(receivers,filename)
