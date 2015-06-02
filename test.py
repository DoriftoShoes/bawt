from switchboard.pin import Pin
from switchboard.board import Board
from bawt.base import Base

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


if __name__ == "__main__":
    zone = int(sys.argv[1])
    state = sys.argv[2]

    irrigation = Irrigation()

    if state == 'on':
        irrigation.start(zone)
    elif state == 'off':
        irrigation.stop(zone)   
