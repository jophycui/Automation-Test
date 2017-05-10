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


class CT(test_env.TestEnv):

    def test_ct(self):
        self.ct = PublicMethod(self.driver)

        if self.FILENAME == 'run_all_ko.py':
            self.ct.generate_access_code(ExamPath_KO.ct)
            self.ct.access(ExamPath_KO.ct)

        elif self.FILENAME == 'run_all_en.py':
            pass
        elif self.FILENAME == 'run_all_cn.py':
            pass
        self.ct.ct_sample_instruction()
        self.ct.ct_sample_exam()
        self.ct.ct_real_exam()

if __name__ == "__main__":
    unittest.main(verbosity=2)
