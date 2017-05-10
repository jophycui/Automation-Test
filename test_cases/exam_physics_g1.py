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


class Physics_G1(test_env.TestEnv):

    def test_physics_g1(self):
        self.pys_g1 = PublicMethod(self.driver)

        if self.FILENAME == 'run_all_ko.py':
            self.pys_g1.generate_access_code(ExamPath_KO.physics_g1)
            self.pys_g1.access(ExamPath_KO.physics_g1)
        elif self.FILENAME == 'run_all_en.py':
            pass
        elif self.FILENAME == 'run_all_cn.py':
            pass
        self.pys_g1.begin_exam()
        self.pys_g1.select_answers()


if __name__ == "__main__":
    unittest.main()
