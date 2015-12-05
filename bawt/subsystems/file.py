from bawt.bawt import Bawt
from bawt.subsystems.s3 import S3

import os

class File(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.remote = self.camera.get('remote', None)
        self.remote_type = self.remote.get('type', None)
        self.logger = self.get_logger(__name__)
       
    def copy(self, file_path, destination, delete=False):

        self.logger.info("Remote type is set to %s" % self.remote_type)
        if self.remote_type == 'S3':
            remote_save = S3()

        try:
            remote_save.save_file(destination, file_path)
        except Exception as e:
            self.logger.critical("ERROR copying to remote - %s: %s" % (self.remote_type, str(e)))
            return False

        if delete:
            self.delete(file_path)

    def delete(self, file_path):
        os.remove(file_path)
        self.logger.info("Deleted local file: %s" % file_path)
