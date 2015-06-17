from switchboard.pin import Pin
from switchboard.board import Board
from bawt.base import Base

from threading import Thread

import time
import sys

class Irrigation(Base):

    def get_zone(self, zone):
        return self.irrigation['zones'][zone]

    def _get_zone_definition(self, zone):
        return self.get_zone(zone)

    def _get_zone_pin(self, zone):
        pin_number = self._get_zone_definition(zone)
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
