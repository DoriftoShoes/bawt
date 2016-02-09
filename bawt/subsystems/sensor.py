from bawt import log as logging
from bawt.bawt import Bawt

LOG = logging.get_logger(__name__)


class Sensor(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
