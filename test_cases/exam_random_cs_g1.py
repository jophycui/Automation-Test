# -*- coding: utf-8 -*- 
'''
Created on 21 Apr 2017

@author: jophy.cui

'''
from selenium import webdriver
import unittest
from public_method import PublicMethod
from pages import *
import time
import conf
from return_config_data import ConfigData
import sys
from common import test_env


class Random_CS_G1(test_env.TestEnv):
    def test_random_cs_g1(self):

        for _ in range(10):

            self.random_cs_g1 = PublicMethod(self.driver)
            if self.FILENAME == 'run_all_ko.py':
                self.random_cs_g1.generate_access_code(ExamPath_KO.random_g1)
                self.random_cs_g1.access(ExamPath_KO.random_g1)
                self.random_cs_g1.insturction_in_email()

            elif self.FILENAME == 'run_all_en.py':
                self.random_cs_g1.generate_access_code(ExamPath_EN.random_g1)
                self.random_cs_g1.access(ExamPath_EN.random_g1)

            elif self.FILENAME == 'run_all_cn.py':
                pass

            self.random_cs_g1.random_exam()


if __name__ == "__main__":
    unittest.main()
