#!/usr/bin/env python
#encoding: utf-8

"""
Defining tasks
"""


from __future__ import absolute_import
import importlib
import os
import records
from celery import chain, group, subtask
from ConfigParser import ConfigParser
from supervision.lib import Camera, Snapshot
from supervision.celery import gpsparser, cameras
from supervision import CONFIG


@cameras.task(name='supervision.tasks.get_image')
def get_image(camera_name, **kwargs):
    """given a camera name, snap a shot"""
    camera = Camera(camera_name)
    return camera.snap(**kwargs)
        
@cameras.task(name='supervision.tasks.download')
def download(cameras):
    """given a list of cameras, get instant snapshot for each"""
    for camera in cameras:
        get_image.delay(
            camera['name'],
            user=camera['username'],
            pwd=camera['password']
            )
        
@cameras.task(name='supervision.tasks.rm')
def rm(filepath):
    """delete a snapshot given its filepath"""
    return Snapshot.remove(filepath)

@cameras.task(name='supervision.tasks.purge_folder')
def purge_folder(camera_name):
    """purging obsolete snapshots of a camera"""
    path = CONFIG.get('camera_{0}'.format(camera_name), 'snapshots_folder')
    try:
        os.mkdir(path)
    except OSError:
        # the folder exists already, so we try to purge it
        filepaths = [os.path.join(path, i) for i in os.listdir(path)]
        if not set(['latest', 'latest_orig']).issubset(set(filepaths)):
            # the latest files are always symbolic links and shall not
            # be purged; their sources too. If only one is missing,
            # we purge the whole folder.
            res = group(
                rm.s(os.path.join(path, filepath))
                for filepath in filepaths
                )()
            return res
        else:
            try:
                dont_purge = [
                    'latest',
                    'latest_orig',
                    os.readlink(os.path.join(path, 'latest')),
                    os.readlink(os.path.join(path, 'latest_orig'))
                    ]
                res = group(
                    rm.s(os.path.join(path, filepath))
                    for filepath in filepaths if not filepath in dont_purge
                    )()
                return res
            except OSError:
                # the sources of symbolic links are missing,
                # we purge the whole folder
                res = group(
                    rm.s(os.path.join(path, filepath))
                    for filepath in filepaths
                    )()
                return res

@cameras.task(name='supervision.tasks.purge')
def purge(cameras):
    """given a list of cameras, purge their folders"""
    for camera in cameras:
        purge_folder.delay(camera['name'])
    return True
