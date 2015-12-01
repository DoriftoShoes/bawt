from switchboard.pin import Pin
from switchboard.board import Board
from subsystems.camera import Camera

import sys

if __name__ == "__main__":
    pic_type = sys.argv[1]

    cam = Camera()
    cam.setup()
    cam.get_picture(name="foo", use_timestamp=True)
