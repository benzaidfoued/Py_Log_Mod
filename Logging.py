#! /usr/bin/env python
import os
from os import makedirs
from os import path
from datetime import datetime
from enum import ENUM

class LogLevel(Enum):
    OFF = 1
    MINIMUM = 2
    NORMAL = 3
    DEBUG = 4

class Logger(object):
    def __init__(self, full_name, log_level=LogLevel.DEBUG):
        module_name = path.splitext(path.basename(full_name))[0]
        self.log_name = module_name + '.log'
        ########### Create Logs subfolder and the logs_folder directory #########
        logs_folder = 'logs'
        if not path.exists(logs_folder):
           makedirs(logs_folder, exist_ok= True)
           
        ####### Create a a full path for my loggin###########
        self.log = path.join(logs_folder, self.log_name)  
        self.create_log()
        self.logging_level = log_level
        
    def create_log(self):
        with open(self.log , mode='w') as log_file:
            log_file.write(self.get_date_time() + '\t\t*** Starting log ***\n')
        log_file.close()        
           
    def get_date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")    ### String formatting for the time  
    def set_logging_level(self, level):
        self.logging_level = level
    
    def write_to_log(self, msg='', log_level=LogLevel.DEBUG):
        if log_level.value > self.logging_level.value:
            return
        with open(self.log , mode='a') as log_file:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
                log_file.write(self.get_date_time() + '\n') # remove leading new lines
            if msg.endswith('\n'):
                log_file.write(self.get_date_time() + '\t\t' + msg)
                log_file.write(self.get_date_time() + '\n') #append trailing newline
            else:
                log_file.write(self.get_date_time() + '\t\t' +  msg + '\n')
        log_file.close()            
           
           
           
if __name__ == '__main__':
 logger = Logger(__file__, log_level=Loglevel.NORMAL)
 logger.write_to_log('Regular log message', log_level=LogLevel.MINIMUM)
 logger.write_to_log('')
 logger.set_logging_level(LogLevel.DEBUG)
