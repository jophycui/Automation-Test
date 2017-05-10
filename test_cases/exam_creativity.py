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
import all_exam_paths
from config import ko
from return_config_data import ConfigData
import sys
from common import test_env


class Creativity(test_env.TestEnv):

    def test_creativity(self):
        self.cr = PublicMethod(self.driver)

        if self.FILENAME == 'run_all_ko.py':
            self.cr.generate_access_code(ExamPath_KO.cr)
            self.cr.access(ExamPath_KO.cr)

        elif self.FILENAME == 'run_all_en.py':
            pass
        elif self.FILENAME == 'run_all_cn.py':
            pass

        self.cr.creativity_answers()

if __name__ == "__main__":
    unittest.main()
