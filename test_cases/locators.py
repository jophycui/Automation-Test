from selenium.webdriver.common.by import By
from return_config_data import ConfigData


# for maintainability we can seperate web objects by page name

class ProctorPageLocs(object):
    PASSWORD = (By.ID, 'password')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'input.btn')


class RegisterPageLocs(object):
    PROCTOR_NAME = (By.ID, 'proctorName')
    UNIVERSITY_IE89 = (By.TAG_NAME, 'option')
    UNIVERSITY_SPAN = (By.CLASS_NAME, 'selectize-input')
    UNIVERSITY_AFTER_SPAN = (By.CLASS_NAME, 'option')
    RETURN_STUDENT_Y = (By.ID, 'isReturningStudents_true')
    RETURN_STUDENT = (By.ID, 'isReturningStudents_false')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'input.btn')


class SessionPageLocs(object):
    SESSION_CODE = (By.CLASS_NAME, "blue_color")


class StudentAccessPageLocs(object):
    EXAM_SESSION_CODE = (By.ID, 'examSessionCode')
    STUDENT_ID = (By.ID, 'studentId')
    TOKEN = (By.ID, 'validationToken')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'input.btn')


class StudentSurveyPageLocs(object):
    FULL_NAME = (By.ID, 'name')
    MAJOR_IE89 = (By.TAG_NAME, 'option')
    MAJOR_SPAN = (By.XPATH, "//*[@id='majorString_field']/dd/div/div[1]")
    MAJOR_AFTER_SPAN = (By.CLASS_NAME, 'option')
    MAJOR_SELECTED = (By.XPATH, "//*[@id='level_field']/dd/div/div[1]")
    #GRADE_NOT_IE89 = (By.CLASS_NAME, 'option')
    GRADE_NOT_IE89 = (By.CSS_SELECTOR,'div.selectize-dropdown-content > div.option')
    SUBMIT_BTN = (By.NAME, 'singleClickButton')


class ExamPageLocs(object):
    START_EXAM_BTN = (By.NAME, 'BeginExam')
    ANSWER_CHECKBOX_IE89 = (By.NAME, 'questionsAnswers[0].answer')
    ANSWER_CHECKBOX_OTHER = (By.CLASS_NAME, 'label_bt')
    ClICK_CALC = (By.CSS_SELECTOR, 'button.basic_fa_btn.calc')
    CLOSE_CALC = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    ClICK_HELP = (By.NAME, 'help_modal')
    #CLOSE_HELP = (By.NAME, 'help_modal')
    CLOSE_HELP = (By.CLASS_NAME, 'close')
    # @property
    # def close_help(self):
    #     if ConfigData.PLATFORM.upper == "IE":
    #         CLOSE_HELP = (By.NAME, 'help_modal')
    #         return CLOSE_HELP
    # # CLOSE_HELP = (By.CSS_SELECTOR, '#exam_help_modal > div > div > div.modal-footer.clearfix > button')
    #     else:
    #         CLOSE_HELP = (By.CSS_SELECTOR, '#exam_help_modal > div > div > div.modal-footer.clearfix > button')
    #         return CLOSE_HELP
    # #CLOSE_HELP = (By.XPATH, "//*[@id='exam_help_modal']/div/div/div[3]/button")
    CLICK_MARK = (By.NAME, "Mark")
    MARKED = (By.CLASS_NAME, "label label-success")
    CLICK_REVIEW = (By.NAME, "ReviewPage")
    CLICK_BACK = (By.NAME, "Back")
    CLICK_NEXT = (By.NAME, "Next")
    CLICK_EXIT = (By.NAME, "Exit")
   # CONFIRM_EXIT = (By.CSS_SELECTOR, "button.btn.btn-primary")
    CONFIRM_EXIT = (By.CSS_SELECTOR, "button.btn.btn-default")



class CreativityPageLocs(object):
    INPUT_TEXT = (By.CLASS_NAME, 'form-control')
    DUMMY_INFO = 'This information is input from automation test'


class InsturctionEPageLocs(object):
    NEXT = (By.NAME, 'Next')
    BEGIN_EXAM = (By.NAME, 'BeginExam')


class EmailLocs(object):
    INPUT_EMAIL = (By.NAME, 'questionsAnswers[0].answer')
    EMAIL_ADDRESS = 'stanford_test@abc.com'
    SUBMIT_EMAIL = (By.NAME, 'Exit')


class CTSampleLocs(object):
    NEXT = (By.NAME, 'Next')
    START_EXAM_BTN = (By.NAME, 'BeginExam')
    EXIT_BTN = (By.NAME, "Exit")
    CONFIRM_EXIT = (By.CSS_SELECTOR, "button.btn.btn-default")

class CTExamPageLocs(object):
    NEXT = (By.NAME, 'Next')
    HIGHLIGHT_ANSWER = (By.NAME, 'sentence highlight')