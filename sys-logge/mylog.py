import logging
import getpass
import sys
import os
import time


class MyLog(object):
    def __init__(self):
        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            self.log_path = os.path.dirname(os.path.curdir + '/logs/')
            if os.path.exists(self.log_path) and os.path.isdir(self.log_path):
                pass
            else:
                os.mkdir(self.log_path)
            rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            log_name = rq + '.log'
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logHand = logging.FileHandler(
                self.log_path + '/' + log_name, encoding='utf-8')
            logHand.setFormatter(formatter)
            logHand.setLevel(logging.INFO)

            logHandSt = logging.StreamHandler()
            logHandSt.setFormatter(formatter)
            self.logger.addHandler(logHand)
            self.logger.addHandler(logHandSt)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug('log-debug')
    mylog.info('log-debug')
    '''
    from mylog import MyLog
    ml=MyLog()
    ml.debug('')
    '''
