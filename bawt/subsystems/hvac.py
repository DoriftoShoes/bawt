import bawt.log as logging

from bawt.switchboard.bawtio import BawtIO

LOG = logging.get_logger(__name__)


class Hvac(BawtIO):

    def __init__(self):
        super(Hvac, self).__init__('hvac')
        self.zones = self.hvac.get('zones', None)

    def get_zone(self, zone):
        return self.zones.get(zone, False)

    def _get_zone_units(self, zone):
        return self.zones.get(zone).get('units', None)

    def start_zone(self, zone, run_time=False):
        units = self._get_zone_units(zone)
        LOG.info("Starting zone %i" % zone)
        self.multi_on(units, run_time)

    def stop_zone(self, zone):
        units = self._get_zone_units(zone)
        LOG.info("Stopping zone %i" % zone)
        self.multi_off(units)
