#!/usr/bin/env python
#encoding: utf-8


import os
import shutil
import supervision
from ConfigParser import ConfigParser
from setuptools import setup, find_packages


setup(
    name="supervision",
    version=supervision.__version__,
    packages=find_packages(),
    author="Thomas Ayih-Akakpo",
    author_email="thomas@ayih-akakapo.org",
    description="Lightweight private data collector",
    long_description=open('README.md').read(),
    install_requires = [
        "requests",
        "celery",
        "Flask",
        "records"
    ],
    include_package_data=True,
    url='http://github.com/drowolath/supervision.git',
)
