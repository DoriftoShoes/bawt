from switchboard.pin import Pin
from switchboard.board import Board
from subsystems.irrigation import Irrigation

import sys

if __name__ == "__main__":
    zone = int(sys.argv[1])
    state = sys.argv[2]
    if len(sys.argv) >= 4:
        run_time = int(sys.argv[3])

    irrigation = Irrigation()

    if state == 'on':
        irrigation.start(zone)
    elif state == 'off':
        irrigation.stop(zone)
    elif state == 'timed':
        irrigation.timed_run(zone, run_time)   
