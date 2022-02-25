#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/23 14:24
import io
import re
import sys

from setuptools import setup


if sys.version_info < (3, 4):
    sys.exit("Sorry, Python < 3.4 is not supported")

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("txffpAssistant/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = \"(.*?)\"', f.read()).group(1)


setup(
    name="txffpAssistant",
    version=version,
    packages=["txffpAssistant", "txffpAssistant.handler"],
    url="https://github.com/Kairu-Madigan/txffpAssistant",
    license="GNU",
    author="fishyues",
    author_email="fishyues",
    description="为解决某票根网工具",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    python_requires=">=3.4",
    # 需要安装的依赖
    install_requires=[
        "lxml>=4.2.3",
        "requests>=2.19.1",
        "PyPDF2>=1.26.0",
        "filetype>=1.0.1",
        "prettytable>=0.7.2",
        "python-dateutil==2.7.3"
    ],
    classifiers=[
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "txffp = txffpAssistant.cli:main",
        ]
    }
)
