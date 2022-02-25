#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/24 23:54

import io
import os
import sys
import tempfile
import zipfile

import filetype


def is_zip(obj):
    kind = filetype.archive(obj)
    if kind.extension == "zip":
        return True
    return False


def get_zipfile(filepath):
    if os.path.isdir(filepath):
        for root, dirs, files in os.walk(filepath):
            for fn in files:
                fp = os.path.join(root, fn)
                with open(fp, "rb") as f:
                    fb = f.read()
                if is_zip(fb):
                    yield fp, fb
    
    elif os.path.isfile(filepath):
        if is_zip(filepath):
            with open(filepath, "rb") as f:
                fb = f.read()
            yield filepath, fb
        else:
            return iter([])
