from switchboard.board import Board
import yaml

class Base():

    def __init__(self):
        self.board = Board()
        self.config = yaml.safe_load(open('conf/zones.yaml'))
