# -*- coding: utf-8 -*-
# @Author : Young Cc
# @Time   : 2021/08/02
# @File   : log.py

import logging
from pathlib import Path
from logging import handlers
from zhaopin_crawler.settings import LOG_PATH

Path(LOG_PATH).mkdir(exist_ok=True, parents=True)  # 自动创建文件夹


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def __init__(
            self, filename=Path(LOG_PATH, "all.log"), level="info", encoding="utf-8", when="midnight", backCount=7,
            fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"):
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志等级
        self.logger.handlers.clear()  # 防止屏幕多次输出日志内容
        formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")  # 设置日志输出格式
        # 使用 TimedRotatingFileHandler 输出到文件
        # interval 是时间间隔，backupCount 是备份文件的个数，如果超过这个个数，就会自动删除
        # when 是间隔的时间单位：S 秒、M 分、H 小时、D 天、W 每星期（interval==0 时代表星期一）、midnight 每天凌晨
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding=encoding)
        th.setLevel(self.level_relations.get(level))
        th.setFormatter(formatter)

        # 使用 StreamHandler 输出到屏幕
        ch = logging.StreamHandler()
        ch.setLevel(self.level_relations.get(level))
        ch.setFormatter(formatter)

        # 添加两个Handler
        self.logger.addHandler(ch)
        self.logger.addHandler(th)


if __name__ == '__main__':
    # 日志调用方法如下：
    # from utils.log import Logger
    # logger = Logger().logger
    logger = Logger().logger
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
