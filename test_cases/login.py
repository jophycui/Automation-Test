# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import conf
import time
from datetime import datetime
import unittest
import sys
import platform
from setuptools.py31compat import unittest_main
from random import choice


#server info
BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, EXECUTOR = conf.browserstack_info()
#proctor page
proctor_url,password,proctor_name,yes_no,access_url,student_id,exam_token,full_name,grade=conf.login_info()

#screenshot info
screenshot_folder =conf.screenshot_info()

capture_sreenshot = screenshot_folder+BROWSER +BROWSER_VERSION+ "_" + "%s"+ datetime.now().strftime("%Y%m%d%H%M%S.%f")+".png"

class Login():
    def generate_access_code(self):
    
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(proctor_url)

        assert "password"== driver.find_element_by_id("password").get_attribute("id")
        driver.implicitly_wait(5)
        driver.find_element_by_id("password").clear(capture_sreenshot%driver.title)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_css_selector("input.btn").click()
        time.sleep(5)
        assert 3==len(driver.find_elements_by_tag_name('dl'))
        #register page
        driver.find_element_by_id("proctorName").clear()
        driver.find_element_by_id("proctorName").send_keys(proctor_name)
        
        driver.get_screenshot_as_file()
        driver.find_element_by_class_name("selectize-input").click()
    #    driver.find_element_by_xpath(university).click()
        uopts = driver.find_elements_by_class_name("option")
        choice(uopts).click()
        driver.find_element_by_id(yes_no).click()
        driver.find_element_by_css_selector("input.btn").click()
   
     
        ACCESS_CODE=driver.find_element_by_class_name("blue_color").text
        driver.find_element_by_id("password").clear(capture_sreenshot%driver.title)
 #       driver.quit()
        return ACCESS_CODE,driver
        time.sleep(5)
    def access(self,student_id,exam_token,grade,ACCESS_CODE):
 #       self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(access_url)
        driver.implicitly_wait(5)
        driver.find_element_by_id("examSessionCode").clear()
        driver.find_element_by_id("examSessionCode").send_keys(ACCESS_CODE)
        driver.find_element_by_id("studentId").clear()
        driver.find_element_by_id("studentId").send_keys(student_id)
        driver.find_element_by_id("examPathToken").clear()
        driver.find_element_by_id("examPathToken").send_keys(exam_token)
        driver.find_element_by_id("password").clear(capture_sreenshot%driver.title)
        driver.find_element_by_css_selector("input.btn").click()
    
        driver.find_element_by_id("name").clear()

        driver.find_element_by_id("name").send_keys(full_name)
        
        #to click on the drop-down list, then the hidden element will be displayed.   
        driver.find_element_by_xpath("//*[@id='majorString_field']/dd/div/div[1]").click()
        mopts = driver.find_elements_by_class_name("option")
        choice(mopts).click()
        driver.find_element_by_xpath("//*[@id='level_field']/dd/div/div[1]/input").click()
        driver.find_element_by_xpath(grade).click()

    
        driver.find_element_by_name("singleClickButton").click()
  
        



