from bawt import log as logging
from bawt.bawt import Bawt

LOG = logging.get_logger(__name__)


class Devices(Bawt):

    def __init__(self, config_dir='conf/'):
        super(self.__class__, self).__init__(config_dir)

    def get_by_name(self):
        pass

    def get_by_id(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def toggle(self):
        pass

    def timed_run(self):
        pass