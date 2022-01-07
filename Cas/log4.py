# -*- coding: utf-8 -*-
import os
import logging.handlers 
log_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'logs' 
#log_dir = 'C:\\'+ 'logs' 
print(log_dir)
if not os.path.isdir(log_dir):
 os.makedirs(log_dir) 
# CONSTANT VARIABLES 
MODULE_NAME = 'my_module'
LOG_LEVEL = 'INFO' 
def get_logger(module_name=MODULE_NAME, log_level=LOG_LEVEL): 
 logging.basicConfig() 
 logger = logging.getLogger(module_name) 
 logger.setLevel(log_level)
 
 # # 按时间回滚 1天换1次, 保留180天
 # time_file_handler = logging.handlers.TimedRotatingFileHandler(
 # log_dir + os.sep + module_name + '_day.log',
 # when='midnight',
 # interval=1,
 # backupCount=180
 # )
 #
 # time_file_handler.suffix = '%Y-%m-%d.log' # 按 天 
 time_file_handler = logging.handlers.TimedRotatingFileHandler(
 log_dir + os.sep + module_name + '_sec.log',
 when='MIDNIGHT',
 interval=1,
 encoding='utf-8',
 backupCount=180
 ) 
 time_file_handler.suffix = '%Y-%m-%d.log' # 按 秒
 formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(funcName)s]-[%(lineno)d]-12s: [%(levelname)s]-8s>> %(message)s')
 time_file_handler.setFormatter(formatter) 
 logger.addHandler(time_file_handler)
 
 # # 按大小回滚
 # file_size_handler = logging.handlers.RotatingFileHandler(
 # log_dir + os.sep + module_name + 'size.log',
 # maxBytes=1024,
 # backupCount=1000,
 # )
 # file_size_handler.setFormatter(formatter)
 # logger.addHandler(file_size_handler) 
 return logger 
if __name__ == '__main__':
 logger = get_logger()
 logger.info('hello')