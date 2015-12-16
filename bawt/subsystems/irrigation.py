import bawt.log as logging

from bawt.switchboard.bawtio import BawtIO

LOG = logging.get_logger(__name__)


class Irrigation(BawtIO):

    def __init__(self):
        super(Irrigation, self).__init__('irrigation')


