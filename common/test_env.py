import unittest
from log import Log
from selenium import webdriver
from test_cases import conf
from test_cases.return_config_data import ConfigData
from test_cases.public_method import PublicMethod
from test_cases.pages import *
import sys


remote_test = False
OS, OS_VERSION, BROWSER, BROWSER_VERSION, FILENAME, EXECUTOR = conf.browserstack_info(sys.argv[1:])

if remote_test:
    browser_stack = webdriver.Remote(command_executor=ConfigData.EXECUTOR, desired_capabilities=ConfigData.desired_cap)
else:
    if BROWSER == 'IE' or BROWSER == 'Ie' or BROWSER == 'ie':
        local_browser = webdriver.Ie()
    elif BROWSER == 'CHROME' or BROWSER == 'Chrome' or BROWSER == 'chrome':
        local_browser = webdriver.Chrome()
    elif BROWSER == 'FIREFOX' or BROWSER == 'Firefox' or BROWSER == 'firefox':
        local_browser = webdriver.Firefox()


class TestEnv(unittest.TestCase):

    def setUp(self):
        # self.logger = Log()
        # self.logger.debug('--------------------Start----------------------')
        self.OS, self.OS_VERSION, self.BROWSER, self.BROWSER_VERSION, self.FILENAME, self.EXECUTOR = conf.browserstack_info(sys.argv[1:])

        if remote_test:
            self.driver = browser_stack
        else:
            self.driver = local_browser

    def tearDown(self):
        # self.logger.debug('---------------------End------------------------')
        self.driver.quit()