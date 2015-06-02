from switchboard.board import Board
import yaml

class Base():

    def __init__(self):
        self.board = Board()
        self.irrigation = yaml.safe_load(open('conf/irrigation.yaml'))
