# -*- coding: utf-8 -*-
'''
Created on 29 May 2016

@author: jophy.cui

'''
from selenium import webdriver
import unittest
from public_method import PublicMethod
from pages import *
import time
import conf
import fast_selenium_back
import all_exam_paths
from config import ko
from return_config_data import ConfigData


BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, FILENAME, EXECUTOR = conf.browserstack_info()


class SampleQL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor=ConfigData.EXECUTOR, desired_capabilities=ConfigData.desired_cap)
        self.cr = PublicMethod(self.driver)

        if FILENAME == 'run_all_ko.py':
            self.cr.generate_access_code(ExamPath_KO.cr)
            self.cr.access(ExamPath_KO.cr)

        elif FILENAME == 'run_all_en.py':
            pass
        elif FILENAME == 'run_all_cn.py':
            pass

    def test_creativity(self):
        self.cr.creativity_answers()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
