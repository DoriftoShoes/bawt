import time

from bawt import log as logging
from bawt.bawt import Bawt
from bawt.switchboard.pin import Pin

LOG = logging.get_logger(__name__)


class Device(Bawt):

    def __init__(self, config_dir='conf/'):
        super(self.__class__, self).__init__(config_dir)

    def get_by_name(self, name):
        device = self.device.get(name, None)
        if not device:
            return False
        return device

    def _get_pin(self, name):
        pin_number = self.get_by_name(name).get('pin', None)
        return Pin(pin_number)

    def on(self, name):
        LOG.info("Enabling device %i" % name)
        pin = self._get_pin(name)
        pin.on()

    def off(self, name):
        LOG.info("Disabling device %i" % name)
        pin = self._get_pin(name)
        pin.off()

    def toggle(self, name):
        LOG.info("Toggling device %i" % name)
        pin = self._get_pin(name)
        pin.toggle()

    def timed_run(self, name, run_time):
        pass

    def moment(self, name):
        moment_length = 2
        LOG.info("Momentary run: %s for %i seconds" % (name, moment_length))
        pin = self._get_pin(name)
        pin.on()
        time.sleep(moment_length)
        pin.off()