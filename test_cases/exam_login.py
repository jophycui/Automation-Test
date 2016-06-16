# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import unittest
from login import Login
import conf


proctor_url,password,proctor_name,university,yes_no,access_url,student_id,exam_token,full_name,major,grade=conf.login_info()
screenshot_folder =conf.screenshot_info()
BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, EXECUTOR = conf.browserstack_info()
desired_cap = {'os': PLATFORM, 'os_version':OS_VERSION, 'browser':BROWSER, 'browser_version': BROWSER_VERSION, 'browserstack.debug':'true'}

class ExamLogin(unittest.TestCase):
    def setUp(self):
        self.exam_login=Login()
        self.ACCESS_CODE,self.driver =self.exam_login.generate_access_code()
        driver = self.driver
    
    def test_empty_values(self):

        driver = self.driver
        driver.get(access_url)
        driver.implicitly_wait(15)
        driver.find_element_by_id("examSessionCode").clear()
        driver.find_element_by_id("examSessionCode").send_keys("")
        driver.find_element_by_id("studentId").clear()
        driver.find_element_by_id("studentId").send_keys("")
        driver.find_element_by_id("examPathToken").clear()
        driver.find_element_by_id("examPathToken").send_keys("")       
        driver.find_element_by_css_selector("input.btn").click()
        errors = driver.find_elements_by_tag_name("d1")
        for e in errors:       
            self.assertEqual("error",e.get_attribute("class"), "Prompt messages are not match")
            
    def test_invalid_values(self):

        driver = self.driver
        driver.get(access_url)
        driver.implicitly_wait(15)
        driver.find_element_by_id("examSessionCode").clear()
        driver.find_element_by_id("examSessionCode").send_keys("invalid")
        driver.find_element_by_id("studentId").clear()
        driver.find_element_by_id("studentId").send_keys("123456")
        driver.find_element_by_id("examPathToken").clear()
        driver.find_element_by_id("examPathToken").send_keys("heise")       
        driver.find_element_by_css_selector("input.btn").click()
        erros_list = driver.find_element_by_tag_name("li")     
        self.assertTrue(erros_list.text, "Error text is NOT exist")
            
    def tearDown(self):
  
        self.driver.quit()

        
if __name__ == "__main__":
    unittest.main()