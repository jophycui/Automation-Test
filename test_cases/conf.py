# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui

'''
from selenium import webdriver
import sys

import random
from random import choice



def login_info(
    proctor_url = "http://52.39.5.178:9000/proctor",
    password = "abcd1234",
    proctor_name = "proctor_name_"+ str(random.randint(0,1000)),
  #  university = ["//*[@id='university_field']/dd/div/div[2]/div/div[1]","//*[@id='university_field']/dd/div/div[2]/div/div[2]","//*[@id='university_field']/dd/div/div[2]/div/div[3]"],
    yes_no = ['isReturningStudents_true','isReturningStudents_false'],    
    access_url = "http://52.39.5.178:9000/student/access",   
    student_id =["US01EE1201B","US01EE1202"],
    exam_token =["red","blue","black","yellow"],
    
    full_name ="test_user_" + str(random.randint(0,1000)),
  #  major = ["//*[@id='majorString_field']/dd/div/div[2]/div/div[1]","//*[@id='majorString_field']/dd/div/div[2]/div/div[2]","//*[@id='majorString_field']/dd/div/div[2]/div/div[3]"],
    grade = ["//*[@id='level_field']/dd/div/div[2]/div/div[1]","//*[@id='level_field']/dd/div/div[2]/div/div[2]"]):
    # after select sudentid, token and grade will based on studentid to choose different path. 

    return proctor_url,password,proctor_name,choice(yes_no),access_url,student_id,exam_token,full_name,grade


def email_info(
    HOST = "smtp.gmail.com",
    PORT="587",
    mail_username = "reportsenderserver@gmail.com",
    mail_password = "test*321",
    to_addrs ="jophycui@gmail.com" ,#stanford@br-clients.flowdock.com
    folder="D:\\eclips\\Educational Software\\Report\\"):
    return HOST,PORT,mail_username,mail_password,to_addrs,folder

def screenshot_info(
    screenshot_folder="D:\\eclips\\Educational Software\\Screenshots\\"):
    return screenshot_folder


def browserstack_info(      
    BROWSER_VERSION = sys.argv.pop(),  
    BROWSER = sys.argv.pop(), 
    OS_VERSION = sys.argv.pop(),                            
    PLATFORM = sys.argv.pop(),



    EXECUTOR = 'http://jophycui2:dTuhA6cxuqCBdfWx8vC3@hub.browserstack.com:80/wd/hub'):
    
    return BROWSER_VERSION,BROWSER,OS_VERSION,PLATFORM,EXECUTOR


#===============================================================================
# def browser_info(
#     BROWSER = sys.argv.pop(),
#     PLATFORM = sys.argv.pop(),
#     SERVER = {'chrome':'http://127.0.0.1:5555/wd/hub',
#               'firefox':'http://127.0.0.1:4444/wd/hub',
#               'internet explorer':'http://127.0.0.1:6666/wd/hub'}):
#  
#     EXECUTOR=SERVER.get(BROWSER,'Please check server configure info')
#     return BROWSER,PLATFORM,EXECUTOR
#===============================================================================