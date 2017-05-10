import conf
import sys


class ConfigData(object):
    OS, OS_VERSION, BROWSER, BROWSER_VERSION, FILENAME, EXECUTOR= conf.browserstack_info(sys.argv[1:])

    #if need to capture browserstack logs, please add 'browserstack.debug': True
    desired_cap = {'os': OS, 'os_version': OS_VERSION, 'browser': BROWSER, 'browser_version': BROWSER_VERSION,
                   'nativeEvents': 'true'}

    screenshot_folder = conf.screenshot_info()

    capture_sreenshot = screenshot_folder + OS + OS_VERSION + "_" + BROWSER + BROWSER_VERSION + "_" + "%s" + "_" + "Q" + "%s" + "_" + "%s" + ".png"

    proctor_url, password, proctor_name, access_url, full_name, grade = conf.login_info()

