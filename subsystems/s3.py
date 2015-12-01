from boto.s3.connection import S3Connection
from boto.s3.key import Key

from bawt.bawt import Bawt

from StringIO import StringIO
import os

class S3(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self._aws_access_key = self.aws.get('access_key', None)
        self._aws_secret_key = self.aws.get('secret_key', None)

    def connect(self):
        conn = None
        if not self._aws_access_key or not self._aws_secret_key:
            raise Exception('AWS Credentials are not set')

        try:
            conn = S3Connection(self._aws_access_key, self._aws_secret_key)
        except Exception as e:
            print str(e)
        return conn

    def _create_or_set_bucket(self, bucket):
        conn = self.connect()
        try:
            b = conn.create_bucket(bucket)
            self._bucket = bucket_name
        except:
            b = conn.get_bucket(bucket)
        return b

    def _create_key(self, key_name, bucket):
        b = self._create_or_set_bucket(bucket)
        k = Key(b)
        k.key = key_name
        return k

    def save_file(self, bucket, file_path):
        file_dir, file_name = os.path.split(file_path)
        k = self._create_key(file_name, bucket)
        k.set_contents_from_file(StringIO(file_path))

    def save_string(self, bucket, name, content):
        k = self._create_key(name, bucket)
        k.set_contents_from_string(contents)

