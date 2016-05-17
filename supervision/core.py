#!/usr/bin/env python
#encoding: utf-8

"""
Some core classes and routines
"""

from __future__ import absolute_import
import os
import requests
import time
from ConfigParser import ConfigParser
from PIL import Image
from StringIO import StringIO
from supervision import CONFIG, CAMERAS


class Camera(object):
    """represents an IP Camera"""
    def __init__(self, name):
        kwargs = filter(lambda x: x['name'] == name, CAMERAS)
        if not kwargs:
            self.exists = False
        else:
            for key, value in kawrgs[0].items():
                vars(self)[key] = value
            self.exists = True

    def snap(self, **kwargs):
        """instant snapshot"""
        try:
            request = requests.get(self.url, params=kwargs, timeout=2)
        except Exception:
            request = requests.models.Response()
        if request.status_code != 200:
            return False
        else:
            print 'OK'
            epoch = time.time()
            original_image_name = '{epoch}_{camera}'.format(
                epoch=epoch, camera=self.name)
            resized_image_name = '{epoch}_resized_{camera}'.format(
                epoch=epoch, camera=self.name)
            try:
                os.mkdir(self.snapshots_folder)
            except OSError:
                pass
            finally:
                im = Image.open(StringIO(request.content))
                im.save(
                    os.path.join(path, original_image_name),
                    'JPEG'
                    )
                im.thumbnail((300, 225), Image.ANTIALIAS)
                im.save(
                    os.path.join(self.snapshots_folder, resized_image_name),
                    'JPEG'
                    )
            try:
                os.remove(os.path.join(self.snapshots_folder 'latest'))
                os.remove(os.path.join(self.snapshots_folder 'latest_orig'))
            except OSError:
                pass
            finally:
                os.symlink(
                    os.path.join(self.snapshots_folder resized_image_name),
                    os.path.join(self.snapshots_folder 'latest')
                    )
                os.symlink(
                    os.path.join(self.snapshots_folder original_image_name),
                    os.path.join(self.snapshots_folder 'latest_orig')
                    )
            return True

        
class Snapshot(object):
    """represents a camera's instant snapshot"""
    def __init__(self, name):
        self.camera = name
        self.folder = CONFIG.get('camera_'+self.camera, 'snapshots_folder')
        try:
            os.mkdir(self.folder)
        except OSError:
            pass # the folder already exists

    @staticmethod
    def remove(filepath):
        try:
            os.remove(filepath)
            return True
        except OSError:
            return False

    def record(self, epoch, data):
        """record a bytestream to image"""
        self.original_image_name = '{epoch}_{camera}'.format(
            epoch=epoch, camera=self.camera)
        self.resized_image_name = '{epoch}_resized_{camera}'.format(
            epoch=epoch, camera=self.camera)
        im = Image.open(StringIO(data))
        im.save(
            os.path.join(self.folder, self.original_image_name),
            'JPEG'
            )
        im.thumbnail((300, 225), Image.ANTIALIAS)
        im.save(
            os.path.join(self.folder, self.resized_image_name),
            'JPEG'
            )
        try:
            os.remove(os.path.join(self.folder, 'latest'))
            os.remove(os.path.join(self.folder, 'latest_orig'))
        except OSError:
            pass
        finally:
            os.symlink(
                os.path.join(self.folder, self.resized_image_name),
                os.path.join(self.folder, 'latest')
                )
            os.symlink(
                os.path.join(self.folder, self.original_image_name),
                os.path.join(self.folder, 'latest_orig')
                )
