from bawt.bawt import Bawt
from bawt.subsystems.s3 import S3

import os

class File(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.remote = self.camera.get('remote', None)
        self.remote_type = self.remote.get('type', None)
       
    def copy(self, file_path, destination, delete=False):
        if self.remote_type == 's3':
            s3 = S3()
            s3.save_file(destination, file_path)

        if delete:
            self.delete(file_path)

    def delete(self, file_path):
        os.remove(file_path)
