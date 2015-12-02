from bawt.bawt import Bawt
from bawt.subsystems.s3 import S3

class File(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.remote = self.camera.get('remote', None)
       
    def copy(self, file_path, destination):
        if self.remote == 's3':
            s3 = S3()
            s3.save_file(destination, file_path)
        
