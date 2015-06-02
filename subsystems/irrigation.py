from switchboard.pin import Pin
from switchboard.board import Board
from bawt.base import Base

from threading import Thread

import time
import sys

class Irrigation(Base):

    def get_zone(self, zone):
        return self.config['zones'][zone]
        
    def start(self, zone):
        zone_definition = self.get_zone(zone)
        pin = Pin(zone_definition['pin'])
        pin.on()
        
    def stop(self, zone):
        zone_definition = self.get_zone(zone)
        pin = Pin(zone_definition['pin'])
        pin.off()

    def timed_run(self, zone, run_time):
        thread = Thread(target=self.start(zone))
        time.sleep(run_time)
        self.stop(zone)
