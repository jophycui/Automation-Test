# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import unittest
from login import Login
from datetime import datetime
from random import choice
import time
import conf
import sys

#server info
BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, EXECUTOR = conf.browserstack_info()
#proctor page
proctor_url,password,proctor_name,yes_no,access_url,student_id,exam_token,full_name,grade=conf.login_info()

#screenshot info
screenshot_folder =conf.screenshot_info()

capture_sreenshot = screenshot_folder+BROWSER +BROWSER_VERSION+ "_" + "%s"+ datetime.now().strftime("%Y%m%d%H%M%S.%f")+".png"


class ExamG1_MP(unittest.TestCase):
  
    def setUp(self):
        self.exam_login=Login()
        self.ACCESS_CODE,self.driver =self.exam_login.generate_access_code()
        driver = self.driver


 

    def test_exampath1y1(self):
  ##      self.exam_login=Login()
        driver = self.driver
 
        self.exam_login.access(student_id[0],exam_token[0],grade[0],self.ACCESS_CODE)
        
        driver.find_element_by_id("password").clear(capture_sreenshot%driver.title)
        self.assertEquals("physicsExamG1", driver.find_element_by_name("examId").get_attribute("value"), "Wrong exam path")

        driver.find_element_by_name("Next").click()
        driver.find_element_by_id("password").clear(capture_sreenshot%driver.title)
        driver.find_element_by_name("BeginExam").click()
        driver.find_element_by_name("Exit").click()
   #     alert = driver.switch_to_alert()

        time.sleep(5)
 #       alert.accept()
        self.assertEquals("mathExamG1", driver.find_element_by_name("examId").get_attribute("value"), "Wrong exam path")
        
        
        #random select an answer and click on next button
#===============================================================================
#         num = 1
#         while num < 5:
# 
#             answers = driver.find_elements_by_name("singleSelectAnswer")
#             checkbox =(choice(answers))
#             checkbox.click()
#   
#             self.assertTrue(checkbox.is_selected(),"not selected")
#             driver.find_element_by_name("nextButton").click()
#             num = num + 1
#===============================================================================
    

    def tearDown(self):
        print 111
        for s in student_id:
            self.driver.get(proctor_url[:24]+"demo/students/clear/"+s)
            
 #       self.driver.quit()


if __name__ == "__main__":
   unittest.main()    
