import argparse
import sys
import time

import bawt.log as logging
from bawt.subsystems.camera import Camera

LOG = logging.get_logger(__name__)


class Timelapsed(Camera):

    def __init__(self, argv):
        self.args = None
        self.parse_args(argv)

        super(Timelapsed, self).__init__(config_dir=self.args.config_dir)

        self.setup()
        self.frequency = self.args.frequency if hasattr(self.args, 'frequency') else self.timelapse.get('frequency', 60)
        self.prefix = self.args.prefix if hasattr(self.args, 'prefix') else self.timelapse.get('prefix', None)
        self.delete = self.args.delete if hasattr(self.args, 'delete') else self.timelapse.get('delete', False)

    def parse_args(self, argv):

        parser = argparse.ArgumentParser(description='timelapse daemon')
        parser.add_argument('--config-dir',
                            dest='config_dir',
                            default='conf/main.yaml',
                            help='path to the config file')
        parser.add_argument('--frequency',
                            dest='frequency',
                            help='Frequency of capture')
        parser.add_argument('--prefix',
                            dest='prefix',
                            help='Filename prefix')
        parser.add_argument('--delete',
                            dest='delete',
                            help='Delete local file')

        self.args = parser.parse_args(args=argv)

    def get_pic(self):
        self.get_picture(name=self.prefix, use_timestamp=True)
        self.remote_save(delete_local=self.delete)

    def run(self):
        if self.timelapse.get('enabled', False):
            while True:
                self.get_pic()
                time.sleep(float(self.frequency))
        else:
            LOG.info('Timelapse is disabled.  Please review your config file.')


def main(argv=sys.argv[1:]):

    timelapsed = Timelapsed(argv)
    timelapsed.run()
