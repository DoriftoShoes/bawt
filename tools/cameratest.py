from bawt.switchboard.pin import Pin
from bawt.switchboard.board import Board
from bawt.subsystems.camera import Camera
from bawt.subsystems.file import File

import sys

if __name__ == "__main__":
    pic_type = sys.argv[1]

    cam = Camera('/Users/phool/git/bawt/conf/')
    cam.setup()
    cam.get_picture(name=pic_type, use_timestamp=True)
 
    cam.remote_save(delete_local=True, remote_target="phool-test")
