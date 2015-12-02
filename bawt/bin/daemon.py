import argparse
import multiprocessing
import sys
import time

from bawt.bawt import Bawt

class Bawtd(Bawt):

    def __init__(self, argv):
        super(self.__class__, self).__init__()
        
        self.parser = argparse.ArgumentParser(description='bawt daemon')
        self.parser.add_argument('--subsystem', dest='subsystem', default=None, help='Subsystem to run')
        self.parser.add_argument('--config-file', dest='config_file', default='conf/main.yaml', help='path to the config file')
        self.args = self.parser.parse_args(args=argv)
        
    def run(self):
        while True:
            print('running')           
            

def main(argv=sys.argv[1:]):

    bawtd = Bawtd(argv)
    bawtd.run()

