import time

try:
    import picamera
except ImportError:
    import bawt.mock.picamera as picamera

from bawt.bawt import Bawt
from bawt.subsystems.file import File


class Camera(Bawt):

    def __init__(self, config_dir='conf/'):
        super(self.__class__, self).__init__(config_dir)
        self.fname = None
        self.remote = None
        self.picture_directory = None
        self.resolution = None
        self.cam = None
        self._is_initialized = None

    def setup(self):
        """
        Setup method to read configs.
        """
        self.fname = None
        self.remote = self.camera.get('remote', None)
        self.picture_directory = self.camera.get('directory', Bawt.DEFAULT_DIRECTORY)
        self.resolution = self.camera.get('resolution', Bawt.DEFAULT_RESOLUTION)
        self.cam = picamera.PiCamera()
        self.cam.resolution = (self.resolution['x'], self.resolution['y'])
        self._is_initialized = False

    def _initialize(self):
        """
        Initialize the camera if it is not yet initialized.
        """
        if not self._is_initialized:
            self.cam.start_preview()
            time.sleep(2)
            self._is_initialized = True
            self.logger = self.get_logger(__name__)

    def _get_filepath(self, name=None, use_timestamp=True):
        """
        Build file path based on config settings, name, and timestamp
        :param name: File name.  Defaults to timestamp
        :param use_timestamp: Whether to include timestamp in filename
        :return:
        """
        current_time = str(int(time.time()))
        if not name and not use_timestamp:
            raise Exception("Name or timestamp is required")
        if name:
            self.fname = "%s" % name
            current_time = "_%s" % current_time
        if use_timestamp:
            self.fname = "%s%s" % (self.fname, current_time)
        if len(self.fname) > 0:
            self.fname = "%s/%s.jpg" % (self.picture_directory, self.fname)
        return self.fname

    def get_picture(self, name=None, use_timestamp=True):
        """
        Take a picture with the rPi camera
        :param name: File name.  If not specified defaults to time
        :param use_timestamp: Whether to include timestamp in filename
        """
        self._get_filepath(name, use_timestamp)
        self._initialize()
        self.logger.info("Taking picture: %s" % self.fname)
        self.camera.capture(self.fname)

    def remote_save(self, file_path=None, delete_local=False, remote_target=None):
        """
        Save to remote system as configured in camera.yaml
        :param file_path: Local path to file
        :param delete_local: Remove from local system after copy
        :param remote_target: Target on remote system (S3 bucket, file path, etc)
        """
        if not file_path:
            file_path = self.fname

        f = File()
        if not remote_target:
            remote_target = self.remote.get('target', None)
        self.logger.info("Saving picture %s to %s" % (file_path, remote_target))
        f.copy(file_path, remote_target, delete=delete_local)
