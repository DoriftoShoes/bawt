from bawt.subsystems.camera import Camera

import sys

if __name__ == "__main__":
    pic_type = sys.argv[1]

    cam = Camera('/home/pi/bawt/conf/')
    cam.setup()
    cam.get_picture(name=pic_type, use_timestamp=True)
 
    cam.remote_save(delete_local=True, remote_target="phool-test")
