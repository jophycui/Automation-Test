# -*- coding: utf-8 -*- 
'''
Created on 29 May 2016

@author: jophy.cui
'''
from selenium import webdriver
import time
from datetime import datetime
from random import choice
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import *
from return_config_data import ConfigData
from pages import *
from all_exam_paths import *
from common.log import Log
from assertions import  *


success = "SUCCESS"
failed = 'FAILED'
local_time = time.asctime(time.localtime(time.time()))


class PublicMethod(BasePage):
    def generate_access_code(self, exam_path):
        """generate access code"""
        try:
            gen_main_page = BasePage(self.driver)
            stu_main_page = StudenAccessPage(self.driver)
            gen_main_page.open_url(ConfigData.access_url + '/demo/students/clear/' + stu_main_page.student_id(exam_path))
            time.sleep(1)
            gen_main_page.open_url(ConfigData.proctor_url)
            self.driver.implicitly_wait(5)
            time.sleep(5)
            pro_main_page = ProctorPage(self.driver)
            pro_main_page.input_password()
            gen_main_page.capture_screenshot()
            pro_main_page.click_submit()
            self.driver.implicitly_wait(5)

            # Regester Page
            reg_main_page = RegisterPage(self.driver)
            reg_main_page.input_proctor_name()
            reg_main_page.select_university()
            reg_main_page.return_student_bool(exam_path)
            time.sleep(1)
            gen_main_page.capture_screenshot()
            reg_main_page.click_submit()


            # Register Session Page
            self.driver.implicitly_wait(5)
            self.wait_for_available(*SessionPageLocs.SESSION_CODE)
            self.ACCESS_CODE = self.driver.find_element(*SessionPageLocs.SESSION_CODE).text
            logger.info('Generate access code successfully')
            return self.ACCESS_CODE, self.driver
        except Exception as e:
            logger.info('Generate access code failed: {}'.format(e))

    def access(self, exam_path):
        """go to access page"""
        try:
            gen_main_page = BasePage(self.driver)
            gen_main_page.open_url(ConfigData.access_url)
            self.driver.implicitly_wait(5)

            # Student acesss page
            stu_main_page = StudenAccessPage(self.driver)
            stu_main_page.input_session_code(self.ACCESS_CODE)
            stu_main_page.input_student_id(exam_path)
            stu_main_page.input_token(exam_path)
            self.capture_screenshot()
            stu_main_page.click_submit()
            # Student survey page
            stu_survey_page = StudentSurvey(self.driver)
            stu_survey_page.input_fullname()
            stu_survey_page.select_major_grade()
            self.capture_screenshot()
            stu_survey_page.click_submit()
            logger.info('submit student information successfully')

        except Exception as e:
            logger.info('submit student information failed: {}'.format(e))

    def insturction_in_email(self):
        ins_page_email = EmailInstrutionPage(self.driver)
        ins_page_email.click_next_btn()
        input_email = EmailPage(self.driver)
        input_email.email_info()

    def begin_exam(self):
        try:
            start_exam_page = CommonExamPage(self.driver)
            start_exam_page.click_start_btn()
            logger.info('start exam')
        except Exception as e:
            logger.info('failed to start exam: {}'.format(e))

    def select_answers(self, questions=35):
        try:
            physics1_exam_page = CommonExamPage(self.driver)
            gen_main_page = BasePage(self.driver)
            num = 1
            while num <= questions:
                physics1_exam_page.select_checkbox()
                gen_main_page.capture_screenshot(num)
                if num % 10 == 0:
                    physics1_exam_page.click_help()

                elif num % 9 == 0:
                    physics1_exam_page.click_mark()

                elif num % 7 == 0:
                    physics1_exam_page.click_review()
                    time.sleep(1)
                    gen_main_page.capture_screenshot('_ReviewPage')
                    physics1_exam_page.click_back_btn()
                time.sleep(1)
                physics1_exam_page.click_next_btn()
                num += 1
            physics1_exam_page.exit_exam()
            gen_main_page.capture_screenshot()
            logger.info('finish exam')
        except Exception as e:
            logger.info('select answer failed: {}'.format(e))

    def faculty_cn(self):
        fa_exam_page = CommonExamPage(self.driver)



    def creativity_answers(self):
        cr_exam_page = CommonExamPage(self.driver)
        gen_main_page = BasePage(self.driver)
        gen_main_page.capture_screenshot()
        cr_exam_page.click_start_btn()
        cr_exam_answers = CreativityExamPage(self.driver)
        time.sleep(10)
        cr_exam_answers.input_text()
        time.sleep(50)
        assert 'part2' in self.get_url
        cr_exam_page.click_start_btn()
        cr_exam_answers.input_text()
        time.sleep(60)
        assert 'submitAnswer' in self.get_url
        gen_main_page.capture_screenshot()

    def ct_sample_instruction(self):
        ct_sample_ins_page = CTSampleInsPage(self.driver)
        ct_sample_ins_page.ct_ins_sample()
        ct_sample_ins_page.start_ct_sample_exam()

    def ct_sample_exam(self):
        ct_sample_exam_page = CTSampleExamPage(self.driver)
        ct_sample_exam_page.ct_sample_exam()
        ct_sample_exam_page.exit_ct_sample_exam()

    def ct_real_exam(self):
        ct_real_exam_page = CTRealExamPage(self.driver)
        ct_real_exam_page.start_real_exam()

    def random_exam(self, num=4):
        time.sleep(2)
        self.begin_exam()
        radom_main_page = BasePage(self.driver)
        current_url_first = radom_main_page.get_url
        if self.FILENAME == 'run_all_en.py':
            if 'RR-G4_EN' in current_url_first:
                return en.RandomExamPath.G1CS_RR_CR
            elif 'PHYS-G1_ENG' in current_url_first:
                return en.RandomExamPath.G1CS_PM
            elif 'MATH-G1_ENG' in current_url_first:
                return en.RandomExamPath.G1CS_MP
            else:
                raise NoSuchExamPath('Exam path is not exist')
        elif self.FILENAME == 'run_all_ko.py':
                if 'RR-G4_KO' in current_url_first:
                    return ko.RandomExamPath.G1CS_CQ
                elif 'PHYS-G1_KO' in current_url_first:
                    self.select_answers(num)
                    self.begin_exam()
                    second_exam = self.get_url
                    assert 'MATH-G1_KO' in second_exam
                    self.select_answers(num)
                    logger.info('exam path is: {}'.format(ko.RandomExamPath.G1CS_PM))
                    return ko.RandomExamPath.G1CS_PM
                elif 'MATH-G1_KO' in current_url_first:
                    self.select_answers(num)
                    self.begin_exam()
                    second_exam = self.get_url
                    assert 'PHYS-G1_KO' in second_exam
                    self.select_answers(num)
                    logger.info('exam path is: {} '.format(ko.RandomExamPath.G1CS_MP))
                    return ko.RandomExamPath.G1CS_MP
                else:
                    raise NoSuchExamPath('Exam path is not exist')


    def select_answers_quantitative(self, calc=False):
        driver = self.driver
        driver.find_element_by_name("BeginExam").click()
        num = 1

        while num <= 25:
            if num == 11 or num == 13 or num == 18 or num == 20 or num == 24:
                driver.find_element_by_name("questionsAnswers[0].answer").send_keys("100")
                time.sleep(2)
                driver.get_screenshot_as_file(
                    self.capture_sreenshot % (driver.title, datetime.now().strftime("%Y%m%d%H%M%S")))

                if calc == True:
                    calc_icon = WebDriverWait(self.driver, 15).until(
                        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.basic_fa_btn.calc")))
                    calc_icon.click()
                    calc_pop = WebDriverWait(self.driver, 15).until(
                        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
                    calc_pop.click()
                    time.sleep(1)

                help_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "help_modal")))
                #           help_icon=WebDriverWait(self.driver,15).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"span.fa.fa-question")))
                help_icon.click()
                help_pop = WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, "//*[@id='exam_help_modal']/div/div/div[3]/button")))

                help_pop.click()

                time.sleep(1)
                mark_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "Mark")))
                mark_icon.click()
                time.sleep(2)
                # verify the mark is working or not
                try:
                    assert "Marked" == driver.find_element_by_css_selector(
                        "span.label.label-success").text, "mark failed"
                except AssertionError as e:
                    print "Marked is failed to click"
                    driver.get_screenshot_as_file(
                        self.capture_sreenshot % ("Error", datetime.now().strftime("%Y%m%d%H%M%S")))

                review_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "ReviewPage")))

                review_icon.click()

                driver.find_element_by_name("Back").click()
                driver.find_element_by_name("Next").click()
                num = num + 1
            else:
                if int(self.BROWSER_VERSION) <= 9:
                    answers = driver.find_elements_by_name("questionsAnswers[0].answer")
                else:
                    answers = driver.find_elements_by_class_name("label_bt")
                checkbox = (choice(answers))
                time.sleep(2)
                driver.implicitly_wait(10)
                checkbox.click()
                # verify if radio button check or not
                checked = False
                all_answers = driver.find_elements_by_name("questionsAnswers[0].answer")
                for i in all_answers:
                    if i.get_attribute("checked") == "true":
                        checked = True
                        break
                    else:
                        checked = False
                assert checked == True
                time.sleep(2)
                driver.implicitly_wait(10)

                if calc == True:
                    calc_icon = WebDriverWait(self.driver, 15).until(
                        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.basic_fa_btn.calc")))
                    calc_icon.click()
                    calc_pop = WebDriverWait(self.driver, 15).until(
                        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
                    calc_pop.click()
                    time.sleep(1)

                help_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "help_modal")))
                #           help_icon=WebDriverWait(self.driver,15).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"span.fa.fa-question")))
                help_icon.click()
                help_pop = WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, "//*[@id='exam_help_modal']/div/div/div[3]/button")))

                help_pop.click()

                time.sleep(1)
                mark_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "Mark")))
                mark_icon.click()
                time.sleep(2)
                driver.get_screenshot_as_file(
                    self.capture_sreenshot % (driver.title, datetime.now().strftime("%Y%m%d%H%M%S")))
                # verify the mark is working or not
                try:
                    assert "Marked" == driver.find_element_by_css_selector(
                        "span.label.label-success").text, "mark failed"
                except AssertionError as e:
                    print "Marked is failed to click"
                    driver.get_screenshot_as_file(
                        self.capture_sreenshot % ("Error", datetime.now().strftime("%Y%m%d%H%M%S")))

                review_icon = WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "ReviewPage")))

                review_icon.click()

                driver.find_element_by_name("Back").click()
                driver.find_element_by_name("Next").click()
                num = num + 1

        driver.get_screenshot_as_file(self.capture_sreenshot % (driver.title, datetime.now().strftime("%Y%m%d%H%M%S")))
        driver.find_element_by_name("Exit").click()
        time.sleep(5)
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.get_screenshot_as_file(self.capture_sreenshot % (driver.title, datetime.now().strftime("%Y%m%d%H%M%S")))
