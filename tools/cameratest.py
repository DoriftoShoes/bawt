from switchboard.pin import Pin
from switchboard.board import Board
from subsystems.camera import Camera
from subsystems.file import File

import sys

if __name__ == "__main__":
    pic_type = sys.argv[1]

    cam = Camera()
    cam.setup()
    cam.get_picture(name=pic_type, use_timestamp=True)
 
    cam.remote_save(cam.fname)
    cam.get_picture(name=pic_type, use_timestamp=False)

    cam.remote_save(cam.fname)
