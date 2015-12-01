from switchboard.board import Board
import yaml

class Bawt(object):

    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = { 'x': 1024,
                           'y': 768 }
    def __init__(self):
        self.board = Board()
        self.irrigation = yaml.safe_load(open('conf/irrigation.yaml'))
        self.camera = yaml.safe_load(open('conf/camera.yaml'))
        self.config = yaml.safe_load(open('conf/main.yaml'))
        self.environment = yaml.safe_load(open('conf/environment.yaml'))

        self.aws = self.config.get('aws', None)
