import unittest
import HTMLTestRunner
import time
from test_cases import *
from common import send_email
from test_data import *
import sys
sys.path.append("\test_cases")




BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, EXECUTOR = conf.browserstack_info()

HOST,PORT,mail_username,mail_password,to_addrs,folder = conf.email_info()

#list that test cases that need to run
alltestcases = [
	exam_login.ExamLogin,
	exam_path.ExamPath
	]

testunit = unittest.TestSuite()

# add cases to suite
for test in alltestcases: 
	testunit.addTest(unittest.makeSuite(test))


now = time.strftime("%Y-%m-%d_%H_%M_%S")

#folder = "D:\\StoreJava\\Educational Software\\Report\\"

filename = folder + now + "_" + BROWSER + BROWSER_VERSION  + '_Test_Report.html'

fp=open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=BROWSER + BROWSER_VERSION +'Smoke Test Result',description='Please see attachment for more details')

runner.run(testunit)
fp.close()


send_email.send_email(HOST,PORT,mail_username,mail_password,to_addrs,folder)    
    
