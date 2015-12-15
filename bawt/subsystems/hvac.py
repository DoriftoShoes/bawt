import multiprocessing

import bawt.log as logging
from bawt.bawt import Bawt
from bawt.switchboard.pin import Pin

LOG = logging.get_logger(__name__)


class Hvac(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.units = self.hvac.get('units', None)
        self.zones = self.hvac.get('zones', None)

    def get_unit(self, unit):
        return self.units.get(unit, False)

    def get_zone(self, zone):
        return self.zones.get(zone, False)

    def _get_unit_pin(self, unit):
        pin_number = self.get_unit(unit).get('pin', None)
        return Pin(pin_number)

    def _get_zone_units(self, zone):
        return self.get_zone(zone).get('units', None)

    def is_unit_enabled(self, unit):
        return self.get_unit(unit).get('enabled', False)

    def start(self, unit):
        if self.is_unit_enabled(unit):
            LOG.info("Starting unit: %i" % unit)
            pin = self._get_unit_pin(unit)
            pin.on()
            return True
        else:
            LOG.debug("Unit: %i is disabled.  Cannot start." % unit)
            return False

    def stop(self, unit):
        if self.is_unit_enabled(unit):
            LOG.info("Stopping unit: %i" % unit)
            pin = self._get_unit_pin(unit)
            pin.off()
            return True
        else:
            LOG.debug("Unit: %i is disabled.  Cannot start." % unit)
            return False

    def start_zone(self, zone):
        units = self._get_zone_units(zone)
        jobs = []
        LOG.info("Starting zone %i" % zone)
        for unit in units:
            p = multiprocessing.Process(target=self.start, args=(unit,))
            jobs.append(p)
            p.start()

    def stop_zone(self, zone):
        units = self._get_zone_units(zone)
        jobs = []
        LOG.info("Stopping zone %i" % zone)
        for unit in units:
            p = multiprocessing.Process(target=self.stop, args=(unit,))
            jobs.append(p)
            p.start()
