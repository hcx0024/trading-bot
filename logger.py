# encoding: utf-8

import logging as lg
import os
from datetime import datetime

def initialize_logger():
    # creating a log folder for the logs
    logs_path = './logs/' # define the path
    try:
        os.mkdir(logs_path)
    except OSError:
        print("creation of directory %s failed - it does not have to be bad" %logs_path)
    else:
        print("Successfully created log directory")

    # remaining each log depending on time
    date = datetime.now().strftime("%Y%m%d - %H%M%S")
    log_name = date + ".log"
    currentLog_path = logs_path + log_name

    # log parameter
    lg.basicConfig(filename=currentLog_path, format='%(asctime)s - %(levelname)s: %(message)s', level=lg.DEBUG)
    lg.getLogger().addHandler(lg.StreamHandler())

    #logging levels: DEBUG, INFO, WARNING, ERROR
    lg.info('Log initialized!')
    #lg.debug('This is a debugging message!')
    #lg.warning('This is a warning message!')
    #lg.error('This is a error message!')
