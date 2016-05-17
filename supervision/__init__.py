#!/usr/bin/env python
#encoding: utf-8


import importlib
import os
import re
import sys
from celery import *
from core import *

__version__ = '0.1'

CONFIG = ConfigParser(allow_no_value=True)
CONFIG.read('/etc/supervision/supervision.ini')
CAMERAS = []

def load_plugins(filepath, names=[]):
    pysearchre = re.compile('.py$', re.IGNORECASE)
    pluginfiles = filter(pysearchre.search, os.listdir(filepath,
                                                       'supervision_plugins'))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, pluginfiles)
    # import parent module / namespace
    importlib.import_module('supervision_plugins')
    modules = []
    for plugin in plugins:
        if not plugin.startswith('__') and plugin in names:
            modules.append(importlib.import_module(
                plugin, package="supervision_plugins"))
    return modules

sections_cameras = filter(lambda x: x.startswith('camera_'),
                          CONFIG.sections())
for section in sections_cameras:
    CAMERAS.append(dict(CONFIG.items(section)))

if CONFIG.has_section('plugins'):
    PLUGIN_FOLDER = CONFIG.get('plugins', 'folder')
    names = filter(lambda x: x!='folder', CONFIG.options('plugins'))
    PLUGINS = load_plugins(PLUGIN_FOLDER, names)


CAMERA_OPTIONS = [
    'username',
    'password',
    'address',
    'url',
    'name',
    'town',
    'snapshots_folder'
    ]

DATABASE_OPTIONS = ['host', 'user', 'password', 'engine', 'dbname']
