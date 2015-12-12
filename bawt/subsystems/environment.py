from bawt.bawt import Bawt
from bawt import log as logging

class Environment(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.sensors = self.environment.get('sensors', None)
        self.logger = logging.get_logger(__name__, self.logging_config)
