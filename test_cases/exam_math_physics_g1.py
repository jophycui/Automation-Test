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
from return_config_data import ConfigData
import sys
from common import test_env


class MathPhysics_G1(test_env.TestEnv):

    def test_mathphyiscs_g1(self):

        self.mathphyiscs_g1 = PublicMethod(self.driver)
        if self.FILENAME == 'run_all_ko.py':
            self.mathphyiscs_g1.generate_access_code(ExamPath_KO.random_g1)
            self.mathphyiscs_g1.access(ExamPath_KO.random_g1)
            self.mathphyiscs_g1.insturction_in_email()

        elif self.FILENAME == 'run_all_en.py':
            self.mathphyiscs_g1.generate_access_code(ExamPath_EN.random_g1)
            self.mathphyiscs_g1.access(ExamPath_EN.random_g1)

        elif self.FILENAME == 'run_all_cn.py':
            pass

        self.mathphyiscs_g1.begin_exam()
        self.mathphyiscs_g1.select_answers()
        self.mathphyiscs_g1.begin_exam()
        self.mathphyiscs_g1.select_answers()

if __name__ == "__main__":
    unittest.main()
