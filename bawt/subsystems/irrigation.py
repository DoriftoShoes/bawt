import time
from threading import Thread

from bawt import log as logging
from bawt.bawt import Bawt
from bawt.switchboard.pin import Pin

LOG = logging.get_logger(__name__)


class Irrigation(Bawt):

    def __init__(self, config_dir='conf/'):
        super(self.__class__, self).__init__(config_dir)

    def get_zone(self, zone):
        return self.irrigation['units'][zone]

    def _get_zone_definition(self, zone):
        return self.get_zone(zone)

    def _get_zone_pin(self, zone):
        pin_number = self._get_zone_definition(zone).get('pin', None)
        return Pin(pin_number)

    def get_runs(self):
        return self.irrigation.get('runs', None)

    def _get_run_definition(self, run):
        return self.get_runs().get(run, None)

    def _get_run_zones(self, run):
        return self._get_run_definition(run).get('zones', None)

    def start(self, zone):
        LOG.info("Starting zone %i" % zone)
        pin = self._get_zone_pin(zone)
        pin.on()

    def stop(self, zone):
        LOG.info("Stopping zone %i" % zone)
        pin = self._get_zone_pin(zone)
        pin.off()

    def timed_run(self, zone, run_time):
        LOG.info("Timed run of %is requested for zone %i" % (run_time, zone))
        thread = Thread(target=self.start(zone))
        thread.daemon = True
        thread.start()
        time.sleep(run_time)
        self.stop(zone)
