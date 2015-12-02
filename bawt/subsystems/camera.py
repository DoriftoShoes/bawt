from bawt.switchboard.pin import Pin
from bawt.switchboard.board import Board
from bawt.subsystems.file import File
from bawt.bawt import Bawt

from threading import Thread

import picamera
import time
import sys

class Camera(Bawt):

    def setup(self):
        self.fname = None
        self.bucket = self.camera.get('s3_bucket', None)
        self.picture_directory = self.camera.get('directory', Bawt.DEFAULT_DIRECTORY)
        self.resolution = self.camera.get('resolution', Bawt.DEFAULT_RESOLUTION)
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.resolution['x'], self.resolution['y'])
        self._is_initialized = False

    def _initialize(self):
        if not self._is_initialized:
            self.camera.start_preview()
            time.sleep(2)
            self._is_initialized = True

    def _get_filepath(self, name=None, use_timestamp=True):
        current_time = str(int(time.time()))
        if not name and not use_timestamp:
            raise Exception("Name or timestamp is required")
        if name:
            self.fname = "%s" % name
            current_time = "_%s" % current_time
        if use_timestamp:
            self.fname = "%s%s" % (self.fname, current_time)
        if len(self.fname) > 0:
            self.fname =  "%s/%s.jpg" % (self.picture_directory, self.fname)

    def get_picture(self, name=None,use_timestamp=True):
        self._get_filepath(name,use_timestamp)
        self._initialize()
        self.camera.capture(self.fname)

    def remote_save(self, filepath):
        file = File()
        file.copy(filepath, self.bucket)