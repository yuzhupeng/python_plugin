#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 22:41
import logging

from functools import wraps
from contextlib import contextmanager


def post_decode(encoding="utf8"):
    def wrap(func):
        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            result = result.decode(encoding)
            return result
        return wrapped_func
    return wrap



def class_log_level(level=logging.DEBUG):
    def wrap(func):
        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            old_level = self.logger.getEffectiveLevel()
            self.logger.setLevel(level)
            result = func(self, *args, **kwargs)
            self.logger.setLevel(old_level)
            return result
        return wrapped_func
    return wrap


@contextmanager
def log_level(logger, level=logging.DEBUG):
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)
