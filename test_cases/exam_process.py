# coding = utf-8 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import unittest
import login
import time


class ExamPath(unittest.TestCase):
    def setUp(self):
        login.generate_access_code(self)
        login.access(self)
        self.driver = webdriver.Firefox()
        
    def test_random_answers(self):        
        driver = self.driver

    def test_same_answers(self):        
        driver = self.driver

    def tearDown(self):
        time.sleep(15)
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()