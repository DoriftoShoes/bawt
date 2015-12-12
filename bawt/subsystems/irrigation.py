import time
from threading import Thread

from bawt.bawt import Bawt
from bawt import log as logging
from bawt.switchboard.pin import Pin


class Irrigation(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.logger = logging.get_logger(__name__, self.logging_config)

    def get_zone(self, zone):
        return self.irrigation['zones'][zone]

    def _get_zone_definition(self, zone):
        return self.get_zone(zone)

    def _get_zone_pin(self, zone):
        pin_number = self._get_zone_definition(zone).get('pin', None)
        return Pin(pin_number)

    def start(self, zone):
        pin = self._get_zone_pin(zone)
        pin.on()

    def stop(self, zone):
        pin = self._get_zone_pin(zone)
        pin.off()

    def timed_run(self, zone, run_time):
        thread = Thread(target=self.start(zone))
        thread.daemon = True
        thread.start()
        time.sleep(run_time)
        self.stop(zone)
