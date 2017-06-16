# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui

#Note: To run this in local, please make sure you change proctor_url,access_url,to_addrs,folder,screenshot_folder

'''
import sys
import random
import argparse


def email_info():
    HOST = "smtp.gmail.com"
    PORT = "587"
    mail_username = "reportsenderserver@gmail.com"  # "reportsenderserver@gmail.com",
    mail_password = "test*321"
    to_addrs = "229871496@qq.com",  # stanford@br-clients.flowdock.com
    folder = "D:\\screenshot_report\\"
    return HOST, PORT, mail_username, mail_password, to_addrs, folder


def screenshot_info():
    screenshot_folder = "D:\\screenshot_report\\"
    return screenshot_folder

def log_file():
    log_folder = "D:\\screenshot_report\\"
    return log_folder


def parse_args(argv):
    '''
    THIS IS TEST
    '''
    parser = argparse.ArgumentParser(description='usage example: python run_all_en.py Windows 7 Ie | python run_all_en.py iPhone MAC "iPhone 6S Plus" --mobile' )
    parser.add_argument('OS', type=str, help='browser | browserName')
    parser.add_argument('OS_VERSION', type=str, help='os_version  | platform')
    parser.add_argument('BROWSER', type=str, help='os | device ')
    parser.add_argument('--BROWSER_VERSION', type=str, help=' browser_version (required for desktop | mobile can be null) ')
    parser.add_argument('--mobile', action='store_true', help='If run with mobile')

    return parser.parse_args(argv)


def browserstack_info(argv):
    args = parse_args(argv)
    BROWSER_VERSION = args.BROWSER_VERSION
    BROWSER = args.BROWSER
    OS_VERSION = args.OS_VERSION
    OS = args.OS
    MOBILE = args.mobile
    FILENAME = sys.argv[0]
    EXECUTOR = 'http://jophycui2:dTuhA6cxuqCBdfWx8vC3@hub.browserstack.com:80/wd/hub'
    return OS, OS_VERSION,BROWSER,BROWSER_VERSION, FILENAME, EXECUTOR, MOBILE


def login_info():
    BROWSER_VERSION, BROWSER, OS_VERSION, PLATFORM, FILENAME, EXECUTOR, MOBILE = browserstack_info(sys.argv[1:])
    demo_1 = "http://demo-1.highereducationlearning.org"
    demo_2 = "http://demo-2.highereducationlearning.org"
    demo_3 = "http://demo-3.highereducationlearning.org"
    demo_4 = "http://demo-4.highereducationlearning.org"

    if FILENAME == 'run_all_ko.py':
        access_url = demo_4
    elif FILENAME == 'run_all_ru.py':
        access_url = demo_3
    elif FILENAME == 'run_all_cn.py':
        access_url = demo_2
    elif FILENAME == 'run_all_en.py':
        access_url = demo_1
    proctor_url = access_url + "/proctor"
    password = "SuperTest42WLD"
    proctor_name = "proctor_name_" + str(random.randint(0, 10000))
    full_name = "test_user_" + str(random.randint(0, 10000))
    grade = [0, 1, 2, 3]

    return proctor_url, password, proctor_name, access_url, full_name, grade[0]
