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


class FACN(test_env.TestEnv):

    def test_fa_cn(self):
        self.fa = PublicMethod(self.driver)

        if self.FILENAME == 'run_all_ko.py':
            self.fa.generate_access_code(ExamPath_KO.ct)
            self.fa.access(ExamPath_KO.ct)

        elif self.FILENAME == 'run_all_en.py':
            pass

        elif self.FILENAME == 'run_all_cn.py':
            print 111
            self.fa.generate_access_code(ExamPath_CN.random_fa)
            self.fa.access(ExamPath_CN.random_fa)


if __name__ == "__main__":
    unittest.main(verbosity=2)
