#!/usr/bin/env python
#encoding: utf-8


from ConfigParser import ConfigParser

__version__ = '0.1'

CONFIG = ConfigParser(allow_no_value=True)
CONFIG.read('/etc/supervision/supervision.ini')
CAMERAS = []
sections_cameras = filter(lambda x: x.startswith('camera_'),
                          CONFIG.sections())
for section in sections_cameras:
    CAMERAS.append(dict(CONFIG.items(section)))
