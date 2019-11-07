import logging
import os
import time
class MyLogger(object):
    def __init__(self, logger):
        # 创建一个logger对象，并为其命名
        self.logger =logging.getLogger(logger)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 创建handler，创建一个输出到屏幕的handler和一个输出到文件的handler
        file_path = os.path.dirname(os.getcwd()) + r'/logs/'
        # 用日期做日志文件名
        tpath = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))+'.log'
        path = file_path + tpath
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.DEBUG)

        filerhandler = logging.FileHandler(path, mode='a', encoding='utf-8', delay=False)
        filerhandler.setLevel(logging.DEBUG)
        # 创建formatter对象，设置日志输出格式
        formatter = logging.Formatter(' %(asctime)s %(levelname)s %(name)s %(pathname)s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        streamhandler.setFormatter(formatter)
        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filerhandler)

    def put_logger(self):
        return self.logger
