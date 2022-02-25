#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 19:37

import logging
import sys


def stream_logger(format=None, dt_format=None, level=20):
    dt_format = dt_format if dt_format else "%Y-%m-%d %H:%M:%S"
    format = format if format else "%(asctime)s %(levelname)+8s: %(message)s"

    logger = logging.getLogger("stream_logger")
    logger.setLevel(level)
    
    formatter = logging.Formatter(format, dt_format)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    
    logger.addHandler(ch)
    
    return logger
