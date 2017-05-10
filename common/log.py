import logging
import time
import os
from test_cases import conf

log_path = conf.log_file()


class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def printconsole(self, level, message):
        # create logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # create handler for logging
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        # create another handler for print to screen
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # log format
        formatter = logging.Formatter('\n %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add handler to logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        # logging records
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        #if comment removed Handler that will trigger browserstack log
        # logger.removeHandler(ch)
        # logger.removeHandler(fh)
        # # close file
        fh.close()

    def debug(self,message):
        self.printconsole('debug', message)

    def info(self,message):
        self.printconsole('info', message)

    def warning(self,message):
        self.printconsole('warning', message)

    def error(self,message):
        self.printconsole('error', message)