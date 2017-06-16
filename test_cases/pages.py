from selenium import webdriver
import time
from datetime import datetime
from locators import *
from return_config_data import ConfigData
from random import choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from all_exam_paths import *
from config import ko
from config import en
from config import cn
from common.log import Log
from errors import *
from selenium import webdriver

success = "SUCCESS"
failed = 'FAILED'
local_time = time.asctime(time.localtime(time.time()))
logger = Log()


class BasePage(ConfigData):
    """Base class to initialize the base page that will be called from all pages"""
    timeout_seconds = 20

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
    @property
    def get_url(self):
        return self.driver.current_url

    def capture_screenshot(self, qustion_num='0'):
        self.driver.get_screenshot_as_file(self.capture_sreenshot % (self.driver.title, str(qustion_num), datetime.now().strftime("%Y%m%d%H%M%S")))

    def print_log(self, msg):
        logger.info(msg)

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def is_visible(self, by, locator):
        if self.is_element_present(by, locator):
            if self.driver.find_element(by, locator).is_displayed():
                return True
            else:
                return False
        else:
            return False

    def is_element_available(self, by, locator):
        if self.is_visible(by, locator):
            return True
        else:
            return False

    def wait_for_available(self, by, locator):
        for i in range(self.timeout_seconds):
            if self.is_element_available(by, locator):
                break
            time.sleep(1)
        else:
            raise WaitForElementError('Wait for available timed out')
        return True

    def wait_for_visible(self, by,  locator):
        for i in range(self.timeout_seconds):
            if self.is_visible(by, locator):
                break
            time.sleep(1)
        else:
            raise WaitForElementError('Wait for visible timed out')
        return True

    def wait_for_hidden(self, by, locator):
        for i in range(self.timeout_seconds):

            if self.is_visible(by, locator):
                time.sleep(1)
            else:
                break
        else:
            raise WaitForElementError('Wait for hidden timed out')
        return True


class ProctorPage(BasePage):
    def input_password(self):
        if self.wait_for_available(*ProctorPageLocs.PASSWORD):
            element = self.driver.find_element(*ProctorPageLocs.PASSWORD)
            element.clear()
            element.send_keys(ConfigData.password)
        else:
            raise WaitForElementError('Input password failed')

    def click_submit(self):
        if self.wait_for_available(*ProctorPageLocs.SUBMIT_BTN):
            element = self.driver.find_element(*ProctorPageLocs.SUBMIT_BTN)
            element.click()
        else:
            raise WaitForElementError('Click submit button on Proctor page failed')


class RegisterPage(BasePage):
    def input_proctor_name(self):
        if self.wait_for_available(*RegisterPageLocs.PROCTOR_NAME):
            element = self.driver.find_element(*RegisterPageLocs.PROCTOR_NAME)
            element.clear()
            element.send_keys(ConfigData.proctor_name)
        else:
            raise WaitForElementError('Input proctor name failed')

    def select_university(self):

        if str(self.BROWSER_VERSION) == 'None':
            self.driver.find_element(*RegisterPageLocs.UNIVERSITY_SPAN).click()
            uopts = self.driver.find_elements(*RegisterPageLocs.UNIVERSITY_AFTER_SPAN)
            choice(uopts).click()

        elif int(self.BROWSER_VERSION) <= 9:
            uopts = self.driver.find_elements(*RegisterPageLocs.UNIVERSITY_IE89)[1:]
            choice(uopts).click()
        else:
            self.driver.find_element(*RegisterPageLocs.UNIVERSITY_SPAN).click()
            uopts = self.driver.find_elements(*RegisterPageLocs.UNIVERSITY_AFTER_SPAN)
            choice(uopts).click()

    def return_student_bool(self, exam_path):
        if "TBD" in exam_path:
            self.driver.find_element(*RegisterPageLocs.RETURN_STUDENT).click()
            return False
        else:
            self.driver.find_element(*RegisterPageLocs.RETURN_STUDENT_Y).click()
            return True

    def click_submit(self):
        self.driver.find_element(*RegisterPageLocs.SUBMIT_BTN).click()


class AccessCodeResultPage(BasePage):
    def get_access_code(self):
        self.ACCESS_CODE = self.driver.find_element(*SessionPageLocs.SESSION_CODE).text


class StudenAccessPage(BasePage):
    """ Sudent Access Page, including seesion code, student id and token'"""

    def input_session_code(self, access_code):
        element = self.driver.find_element(*StudentAccessPageLocs.EXAM_SESSION_CODE)
        element.clear()
        element.send_keys(access_code)

    def student_id(self, exam_path):

        if exam_path == ExamPath_KO.math_g1:
            return ko.AccessInfo.math_g1_student_id

        elif exam_path == ExamPath_KO.physics_g1:
            return ko.AccessInfo.physics_g1_student_id

        elif exam_path == ExamPath_KO.physics_g3:
            return ko.AccessInfo.physics_g3_student_id

        elif exam_path == ExamPath_KO.math_g3:
            return ko.AccessInfo.math_g3_student_id

        elif exam_path == ExamPath_KO.cr:
            return ko.AccessInfo.cr_student_id

        elif exam_path == ExamPath_KO.ct:
            return ko.AccessInfo.ct_student_id

        elif exam_path == ExamPath_KO.random_g1:
            return ko.AccessInfo.random_student_id

        elif exam_path == ExamPath_EN.random_g1:
            return en.AccessInfo.random_student_id

        elif exam_path == ExamPath_CN.random_fa:
            return cn.AccessInfo.random_faculty_id

    def input_student_id(self, exam_path):
        element = self.driver.find_element(*StudentAccessPageLocs.STUDENT_ID)
        element.clear()
        element.send_keys(self.student_id(exam_path))
        # if exam_path == ExamPath_KO.math_g1:
        #     element.send_keys(ko.AccessInfo.math_g1_student_id)
        #
        # elif exam_path == ExamPath_KO.physics_g1:
        #     element.send_keys(ko.AccessInfo.physics_g1_student_id)
        #
        # elif exam_path == ExamPath_KO.physics_g3:
        #     element.send_keys(ko.AccessInfo.physics_g3_student_id)
        #
        # elif exam_path == ExamPath_KO.math_g3:
        #     element.send_keys(ko.AccessInfo.math_g3_student_id)
        #
        # elif exam_path == ExamPath_KO.cr:
        #     element.send_keys(ko.AccessInfo.cr_student_id)
        #
        # elif exam_path == ExamPath_KO.ct:
        #     element.send_keys(ko.AccessInfo.ct_student_id)
        #
        # elif exam_path == ExamPath_KO.random_g1:
        #     element.send_keys(ko.AccessInfo.random_student_id)
        #
        # elif exam_path == ExamPath_EN.random_g1:
        #     element.send_keys(en.AccessInfo.random_student_id)

    def input_token(self, exam_path):
        element = self.driver.find_element(*StudentAccessPageLocs.TOKEN)
        element.clear()
        if exam_path == ExamPath_KO.math_g1:
            element.send_keys(ko.AccessInfo.math_g1_token)

        elif exam_path == ExamPath_KO.physics_g1:
            element.send_keys(ko.AccessInfo.physics_g1_token)

        elif exam_path == ExamPath_KO.physics_g3:
            element.send_keys(ko.AccessInfo.physics_g3_token)

        elif exam_path == ExamPath_KO.math_g3:
            element.send_keys(ko.AccessInfo.math_g3_token)

        elif exam_path == ExamPath_KO.cr:
            element.send_keys(ko.AccessInfo.cr_token)

        elif exam_path == ExamPath_KO.ct:
            element.send_keys(ko.AccessInfo.ct_token)

        elif exam_path == ExamPath_KO.random_g1:
            element.send_keys(ko.AccessInfo.random_token)

        elif exam_path == ExamPath_EN.random_g1:
            element.send_keys(en.AccessInfo.random_token)
        elif exam_path == ExamPath_CN.random_fa:
            element.send_keys(cn.AccessInfo.random_faculty_token)

    def click_submit(self):

        if self.wait_for_available(*StudentAccessPageLocs.SUBMIT_BTN):
            element = self.driver.find_element(*StudentAccessPageLocs.SUBMIT_BTN)
            time.sleep(1)
            element.click()
        else:
            raise WaitForElementError('Click submit button failed')


class StudentSurvey(BasePage):
    def input_fullname(self):
        element = self.driver.find_element(*StudentSurveyPageLocs.FULL_NAME)
        element.clear()
        element.send_keys(ConfigData.full_name)

    def select_major_grade(self):
        if str(self.BROWSER_VERSION) == 'None':
            self.driver.find_element(*StudentSurveyPageLocs.MAJOR_SPAN).click()
            mopts = self.driver.find_elements(*StudentSurveyPageLocs.MAJOR_AFTER_SPAN)
            choice(mopts).click()
            self.driver.find_element(*StudentSurveyPageLocs.MAJOR_SELECTED).click()
            lopts = self.driver.find_elements(*StudentSurveyPageLocs.GRADE_NOT_IE89)
            time.sleep(1)
            # grades = lopts[2:]
            lopts[2:][self.grade].click()

        elif int(self.BROWSER_VERSION) <= 9:
            mlopts = self.driver.find_element(*StudentSurveyPageLocs.MAJOR_IE89)
            major = mlopts[1:len(mlopts) - 3]
            choice(major).click()
            level = mlopts[2:]
            level[self.grade].click()
            return level

        else:
            self.driver.find_element(*StudentSurveyPageLocs.MAJOR_SPAN).click()
            mopts = self.driver.find_elements(*StudentSurveyPageLocs.MAJOR_AFTER_SPAN)
            choice(mopts).click()
            self.driver.find_element(*StudentSurveyPageLocs.MAJOR_SELECTED).click()
            lopts = self.driver.find_elements(*StudentSurveyPageLocs.GRADE_NOT_IE89)
            time.sleep(1)
            # grades = lopts[2:]
            lopts[2:][self.grade].click()
            # return grades, mopts

    def click_submit(self):
        if self.wait_for_available(*StudentSurveyPageLocs.SUBMIT_BTN):
            self.driver.find_element(*StudentSurveyPageLocs.SUBMIT_BTN).click()
        else:
            raise WaitForElementError('Click on grade submit button failed')


class CommonExamPage(BasePage):
    def click_start_btn(self):
        if self.wait_for_available(*ExamPageLocs.START_EXAM_BTN):
            self.driver.find_element(*ExamPageLocs.START_EXAM_BTN).click()

    def wait_page_loaded(self):
        self.wait_for_available(*ExamPageLocs.ClICK_HELP)
        self.wait_for_available(*ExamPageLocs.CLICK_MARK)
        self.wait_for_available(*ExamPageLocs.CLICK_NEXT)
        self.wait_for_available(*ExamPageLocs.CLICK_REVIEW)
        return self

    def select_checkbox(self):
        if str(self.BROWSER_VERSION) == 'None':
            if self.wait_for_available(*ExamPageLocs.ANSWER_CHECKBOX_OTHER):
                answers = self.driver.find_elements(*ExamPageLocs.ANSWER_CHECKBOX_OTHER)
            else:
                raise WaitForElementError('Find checkbox failed')

        elif int(self.BROWSER_VERSION) <= 9:
            if self.wait_for_available(*ExamPageLocs.ANSWER_CHECKBOX_IE89):
                answers = self.driver.find_elements(*ExamPageLocs.ANSWER_CHECKBOX_IE89)
            else:
                raise WaitForElementError('Find checkbox failed')
        else:
            if self.wait_for_available(*ExamPageLocs.ANSWER_CHECKBOX_OTHER):
                answers = self.driver.find_elements(*ExamPageLocs.ANSWER_CHECKBOX_OTHER)
            else:
                raise WaitForElementError('Find checkbox failed')
        checkbox = (choice(answers))
        checkbox.click()

    def click_calc(self):
        calc_icon = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(ExamPageLocs.ClICK_CALC))
        calc_icon.click()
        calc_pop = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(ExamPageLocs.CLOSE_CALC))
        calc_pop.click()
        time.sleep(2)

    def click_help(self):
        if self.wait_for_available(*ExamPageLocs.ClICK_HELP):
            help_icon = self.driver.find_element(*ExamPageLocs.ClICK_HELP)
            help_icon.click()
        else:
            raise WaitForElementError('Open help failed')
        if self.wait_for_available(*ExamPageLocs.CLOSE_HELP):
            help_close = self.driver.find_element(*ExamPageLocs.CLOSE_HELP)
            help_close.click()
        else:
            raise WaitForElementError('Close help page failed')

    def click_mark(self):

        if self.wait_for_available(*ExamPageLocs.CLICK_MARK):
            mark_icon = self.driver.find_element(*ExamPageLocs.CLICK_MARK)
            mark_icon.click()
            time.sleep(2)
        else:
            raise WaitForElementError('Wait to click on mark error.')

    def click_review(self):
        review_icon = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(ExamPageLocs.CLICK_REVIEW))
        review_icon.click()

    def click_back_btn(self):

        if self.wait_for_available(*ExamPageLocs.CLICK_BACK):
            back_btn = self.driver.find_element(*ExamPageLocs.CLICK_BACK)
            back_btn.click()
        else:
            raise WaitForElementError('Click on next button failed')
        # back_btn = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(ExamPageLocs.CLICK_BACK))
        # back_btn.click()

    def click_next_btn(self):
        if self.wait_for_available(*ExamPageLocs.CLICK_NEXT):
            next_btn = self.driver.find_element(*ExamPageLocs.CLICK_NEXT)
            next_btn.click()
        else:
            raise WaitForElementError('Click on next button failed')

    def exit_exam(self):
        if self.wait_for_available(*ExamPageLocs.CLICK_EXIT):
            self.driver.find_element(*ExamPageLocs.CLICK_EXIT).click()
            if self.wait_for_available(*ExamPageLocs.CONFIRM_EXIT):
                self.driver.find_element(*ExamPageLocs.CONFIRM_EXIT).click()
            else:
                raise WaitForElementError('Click on confirm exit failed')
        else:
            raise WaitForElementError('Click on exit button failed')


class CreativityExamPage(BasePage):
    def input_text(self):
        elements = self.driver.find_elements(*CreativityPageLocs.INPUT_TEXT)
        for e in elements[:-1]:
            time.sleep(10)
            e.send_keys(CreativityPageLocs.DUMMY_INFO)
            self.capture_screenshot()


class EmailInstrutionPage(BasePage):
    def click_next_btn(self):
        if self.wait_for_available(*InsturctionEPageLocs.NEXT):
            next_btn = self.driver.find_element(*InsturctionEPageLocs.NEXT)
            next_btn.click()
        else:
            raise NoSuchElementException('Can NOT click on next')
        if self.wait_for_available(*InsturctionEPageLocs.BEGIN_EXAM):
            start_exam = self.driver.find_element(*InsturctionEPageLocs.BEGIN_EXAM)
            start_exam.click()
        else:
            raise NoSuchElementException('Can NOT click on start exam')


class EmailPage(BasePage):
    def email_info(self):
        input_email = self.driver.find_element(*EmailLocs.INPUT_EMAIL)
        input_email.send_keys(EmailLocs.EMAIL_ADDRESS)
        submit_email = self.driver.find_element(*EmailLocs.SUBMIT_EMAIL)
        submit_email.click()


class CTSampleInsPage(BasePage):
    def ct_ins_sample(self):
        page_num = 1
        while page_num < 10:
            next_btn = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(CTSampleLocs.NEXT))
            if len(next_btn) > 1:
                self.capture_screenshot()
                next_btn[1].click()
            else:
                self.capture_screenshot()
                next_btn[0].click()
            time.sleep(1)
            page_num += 1

    def start_ct_sample_exam(self):
        time.sleep(1)
        click_start_btn = self.driver.find_element(*CTSampleLocs.START_EXAM_BTN)
        click_start_btn.click()


class CTSampleExamPage(BasePage):
    def ct_sample_exam(self):
        page_num = 1
        while page_num < 9:
            next_btn = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(CTSampleLocs.NEXT))
            if len(next_btn) > 1:
                self.capture_screenshot()
                next_btn[1].click()
            else:
                self.capture_screenshot()
                next_btn[0].click()
            time.sleep(1)
            page_num += 1

    def exit_ct_sample_exam(self):
        time.sleep(1)
        click_exit_btn = self.driver.find_element(*CTSampleLocs.EXIT_BTN)
        click_exit_btn.click()
        time.sleep(1)
        self.capture_screenshot()
        confirm_exit = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(CTSampleLocs.CONFIRM_EXIT))
        confirm_exit.click()


class CTRealExamPage(BasePage):
    def start_real_exam(self):
        next_real_exam = self.driver.find_element(*CTSampleLocs.NEXT)
        self.capture_screenshot()
        next_real_exam.click()
        start_real_exam = self.driver.find_element(*CTSampleLocs.START_EXAM_BTN)
        time.sleep(1)
        self.capture_screenshot()
        start_real_exam.click()

class QG1QuestonnairePage(BasePage):
    def exit_qn(self):
        pass

# class RandomExamPage(BasePage):
#
#     def random_exam_path(self, major, grade):
#         sur = StudentSurvey()
#         self.major, self.grade = sur.select_major_grade
#         reg_main_page = RegisterPage(self.driver)
#         if reg_main_page.return_student_bool():
#             if self.grade[grade]:
#                 pass
