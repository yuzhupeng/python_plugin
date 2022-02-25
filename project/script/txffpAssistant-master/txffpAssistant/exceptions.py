#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 16:15


class BaseError(Exception):
    pass


class NotValidMethodError(BaseError):
    """无效的方法"""
    pass


class NoneResponseError(BaseError):
    """请求返回空内容"""
    pass


class ParameterError(BaseError):
    """参数错误"""
    pass


class AuthFailedError(BaseError):
    """认证失败"""
    pass


if __name__ == "__main__":
    raise NotValidMethodError("method is not supported")
