# -*- coding: utf-8 -*- 

import unittest
import HTMLTestRunner
import time
from test_cases import *
from common import send_email
import test_cases.fast_selenium_back
import cases_list
from test_cases.return_config_data import ConfigData
from selenium import webdriver
import sys
from test_cases import conf
sys.path.append("\\test_cases")

#precondition
OS, OS_VERSION,BROWSER,BROWSER_VERSION, FILENAME, EXECUTOR = conf.browserstack_info(sys.argv[1:])
HOST, PORT, mail_username, mail_password, to_addrs, folder = conf.email_info()
proctor_url, password, proctor_name, access_url, full_name, grade = conf.login_info()

#reset env
# driver = webdriver.Remote(command_executor=ConfigData.EXECUTOR, desired_capabilities=ConfigData.desired_cap)
# driver.get(access_url + "/demo/students/clear/deleteAllStudents")
# driver.quit()



# list that test cases that need to run
alltestcases = cases_list.case_list()

testunit = unittest.TestSuite()

# add cases to suite
print "start to run test cases...."
for test in alltestcases:
    testunit.addTest(unittest.makeSuite(test))
    print test

now = time.strftime("%Y-%m-%d_%H_%M_%S")

filename = folder + now + "_" + OS + OS_VERSION + "_" + BROWSER + BROWSER_VERSION + '_Test_Report.html'

fp = open(filename, 'w')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=OS + OS_VERSION + "_" + BROWSER + BROWSER_VERSION + '_Smoke Test Result',
                                       description='Please see attachment for more details')

runner.run(testunit)
print "Writing Report"
fp.close()

#send email
# send_email.send_email(HOST, PORT, mail_username, mail_password, to_addrs, folder)
