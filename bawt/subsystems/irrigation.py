import time
from threading import Thread

from bawt import log as logging
from bawt.bawt import Bawt
from bawt.switchboard.pin import Pin

LOG = logging.get_logger(__name__)


class Irrigation(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.zones = self.irrigation.get('zones', None)

    def get_zone(self, zone):
        return self.zones.get(zone, False)

    def _get_zone_definition(self, zone):
        return self.get_zone(zone)

    def _get_zone_pin(self, zone):
        pin_number = self.get_zone(zone).get('pin', None)
        return Pin(pin_number)

    def is_zone_enabled(self, zone):
        return self.get_zone(zone).get('enabled', False)

    def start(self, zone):
        if self.is_zone_enabled(zone):
            LOG.info("Starting zone: %i" % zone)
            pin = self._get_zone_pin(zone)
            pin.on()
            return True
        else:
            LOG.debug("Zone: %i is disabled.  Cannot start." % zone)
            return False

    def stop(self, zone):
        if self.is_zone_enabled(zone):
            LOG.info("Stopping zone: %i" % zone)
            pin = self._get_zone_pin(zone)
            pin.off()
            return True
        else:
            LOG.debug("Zone: %i is disabled.  Cannot start." % zone)
            return False

    def timed_run(self, zone, run_time):
        thread = Thread(target=self.start(zone))
        thread.daemon = True
        thread.start()
        time.sleep(run_time)
        self.stop(zone)
