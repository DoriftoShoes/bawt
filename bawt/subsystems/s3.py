from boto.s3.connection import S3Connection
from boto.s3.key import Key
from bawt.bawt import Bawt
from StringIO import StringIO
from filechunkio import FileChunkIO
import math
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

    def _get_destination(self, destination):
        return self.camera['destinations'].get(destination, None)

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
        return k,b

    def save_file(self, bucket, file_path):
        file_size = os.stat(file_path).st_size
        file_dir, file_name = os.path.split(file_path)
        file_string = StringIO(file_path)

        k,b = self._create_key(file_name, bucket)
        mp = b.initiate_multipart_upload(file_name)
        chunk_size = 52428800
        chunk_count = int(math.ceil(file_size / float(chunk_size)))
        for i in range(chunk_count):
            offset = chunk_size * i
            bytes = min(chunk_size, file_size - offset)
            with FileChunkIO(file_path, 'r', offset=offset, bytes=bytes) as fp:
                mp.upload_part_from_file(fp, part_num=i + 1)
        mp.complete_upload()
        #k.set_contents_from_file(StringIO(file_path))

    def save_string(self, bucket, name, content):
        k = self._create_key(name, bucket)
        k.set_contents_from_string(contents)
