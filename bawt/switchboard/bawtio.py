import multiprocessing
import time

import bawt.log as logging
from bawt.bawt import Bawt
from bawt.switchboard.pin import Pin

LOG = logging.get_logger(__name__)


class BawtIO(Bawt):

    def __init__(self, subsystem):
        super(self.__class__, self).__init__()
        self.config = getattr(self, subsystem)
        self.units = self.config.get('units', None)
        if not self.units:
            LOG.warning("%s subsystem has no units configured" % subsystem)

    def get_unit(self, unit):
        return self.units.get(unit, False)

    def on(self, unit, run_time=False):
        definition = self.get_unit(unit)
        name = self.get_name(definition)
        if not self.is_enabled(definition):
            LOG.debug("Unit: %s is disabled.  Cannot start." % name)
            return False

        pin = self.get_pin(definition)
        pin.on()
        LOG.info("Started unit: %s" % name)
        if run_time:
            LOG.info("Unit will run for %i seconds" % run_time)
            time.sleep(run_time)
            pin.off()
        return True

    def off(self, unit):
        definition = self.get_unit(unit)
        name = self.get_name(definition)
        if not self.is_enabled(definition):
            LOG.debug("Unit: %s is disabled.  Cannot start." % name)
            return False

        pin = self.get_pin(definition)
        pin.off()
        LOG.info("Stopped unit: %s" % name)
        return True

    def multi_on(self, units, run_time=False):
        jobs = []
        for unit in units:
            p = multiprocessing.Process(target=self.on, args=(unit, run_time))
            jobs.append(p)
            p.start()

    def multi_off(self, units):
        jobs = []
        for unit in units:
            p = multiprocessing.Process(target=self.off, args=(unit,))
            jobs.append(p)
            p.start()

    def get_pin(self, unit):
        definition = self.get_unit(unit)
        pin_number = definition.get('pin', False)
        return Pin(pin_number)

    def get_name(self, unit):
        definition = self.get_unit(unit)
        return definition.get('name', None)

    def is_enabled(self, unit):
        definition = self.get_unit(unit)
        return definition.get('enabled', False)
