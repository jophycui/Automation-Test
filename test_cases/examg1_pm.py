# coding = utf-8 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import unittest
from login import Login
from random import choice
import time
import conf
import sys

BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, EXECUTOR = conf.browserstack_info()
screenshot_folder =conf.screenshot_info()
proctor_url,password,proctor_name,yes_no,access_url,student_id,exam_token,full_name,grade=conf.login_info()
#desired_cap = {'os': PLATFORM, 'os_version':OS_VERSION, 'browser':BROWSER, 'browser_version': BROWSER_VERSION, 'browserstack.debug':'true'}

class ExamG1_MP(unittest.TestCase):
  
    def setUp(self):
        self.exam_login=Login()
        self.ACCESS_CODE,self.driver =self.exam_login.generate_access_code()
        driver = self.driver



 

    def test_exampath1y1(self):
  ##      self.exam_login=Login()
        driver = self.driver
 
        self.exam_login.access(student_id[0],exam_token[0],grade[0],self.ACCESS_CODE)
     
        self.assertEquals("mathExamG1", driver.find_element_by_name("examId").get_attribute("value"), "Wrong exam path")
        driver.get_screenshot_as_file(screenshot_folder+BROWSER +BROWSER_VERSION+ "_"+driver.current_url[24:].replace("/","_")+".png")
        driver.find_element_by_name("Next").click()
        driver.find_element_by_name("BeginExam").click()
        driver.find_element_by_name("Exit").click()
        alert = driver.switch_to_alert()
        alert.accept()
        self.assertEquals("physicsExamG1", driver.find_element_by_name("examId").get_attribute("value"), "Wrong exam path")
           
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

    #===========================================================================
    # def test_physic_g4(self):
    #     pass
    # 
    # def test_physic_g3(self):
    #     pass
    #===========================================================================
    

    def tearDown(self):

                        
        self.driver.quit()


if __name__ == "__main__":
   unittest.main()    
