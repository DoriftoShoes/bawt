from bawt.bawt import Bawt
from bawt import log as logging

LOG = logging.get_logger(__name__)


class Environment(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.sensors = self.environment.get('sensors', None)
