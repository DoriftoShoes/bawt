import time

try:
    import picamera
    testcam = picamera.PiCamera()
    testcam.close()
except:
    import bawt.mock.picamera as picamera
    print picamera.PiCamera.ANNOUNCEMENT

from bawt.bawt import Bawt
import bawt.log as logging
from bawt.subsystems.file import File

LOG = logging.get_logger(__name__)


class Camera(Bawt):

    CONNECTION_RETRIES = 10

    def __init__(self, config_dir='conf/'):
        super(Camera, self).__init__(config_dir)
        self.fname = None
        self.remote = None
        self.picture_directory = None
        self.resolution = None
        self.timelapse = None
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
        LOG.info("Picture directory set to: %s" % self.picture_directory)
        LOG.info("Resolution set to %s" % self.resolution)
        self.timelapse = self.camera.get('timelapse', None)
        self._is_initialized = False

    def connect(self, retries):
        for i in range(0, retries):
            try:
                self.cam = picamera.PiCamera()
            except picamera.PiCamera.PiCameraMMALError as e:
                LOG.debug("Attempt %i connecting to camera. Error: %s" % (retries, str(e)))
                time.sleep(2)

    def _initialize(self):
        """
        Initialize the camera if it is not yet initialized.
        """
        if not self._is_initialized:
            self.connect(retries=Camera.CONNECTION_RETRIES)
            self.cam.resolution = (self.resolution['x'], self.resolution['y'])
            self.cam.start_preview()
            time.sleep(2)
            self._is_initialized = True

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
        LOG.info("Taking picture: %s" % self.fname)
        self.cam.capture(self.fname)
        self.close()

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
        LOG.info("Saving picture %s to %s" % (file_path, remote_target))
        f.copy(file_path, remote_target, delete=delete_local)

    def close(self):
        self.cam.close()
        self._is_initialized = False
