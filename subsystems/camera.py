from switchboard.pin import Pin
from switchboard.board import Board
from bawt.base import Base

from threading import Thread

import picamera
import time
import sys

class Camera(Base):
    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = { 'x': 1024,
                           'y': 768 }

    def setup(self):
        self.picture_directory = self.camera.get('directory', DEFAULT_DIRECTORY)
        self.resolution = self.camera.get('resolution', DEFAULT_RESOLUTION)
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.resolution['x'], self.resolution['y'])
        self._is_initialized = False

    def _initialize(self):
        if not self._is_initialized:
            self.camera.start_preview()
            time.sleep(2)
            self._is_initialized = True

    def _get_filename(self, name=None, use_timestamp=True):
        current_time = time.time()
        fname = None
        if name:
            fname = "%s_" % name
        if use_timestamp:
            fname = "%s%d" % (fname, current_time)
        if len(fname) > 0:
            return "%s.jpg" % fname
        else:
            raise Exception("Name or timestamp is required")

    def get_picture(self, name=None,use_timestamp=True):
        fname = self._get_filename(name,use_timestamp)
        self._initialize()
        self.camera.capture(fname)
