# -*- coding:utf-8; tab-width:4; mode:python -*-

# Taken from Atheist Project

import logging
logging.basicConfig(level=100) # avoid logging messages from other loggers


DATEFORMAT = '%d/%m/%y %H:%M:%S'

class NullHandler(logging.Handler):
    def emit(self, record):
        pass


class CapitalLoggingFormatter(logging.Formatter):
    '''
    define variable "levelcapital" for message formating. You can do things like:
    [EE] foo bar
    '''

    def format(self, record):
        record.levelcapital = record.levelname[0]*2
        return logging.Formatter.format(self, record)


def create_basic_handler():
    formatter = CapitalLoggingFormatter('[%(levelcapital)s] %(message)s', DATEFORMAT)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    return console

def create_logger(name):
    retval = logging.getLogger(name)
    if not retval.handlers:
        retval.addHandler(create_basic_handler())
        retval.propagate = 0
        retval.setLevel(logging.WARNING)
    return retval


Log = create_logger('impinstaller')
