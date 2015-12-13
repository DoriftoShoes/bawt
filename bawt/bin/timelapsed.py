import argparse
import sys
import time
from datetime import datetime

import bawt.log as logging
from bawt.subsystems.camera import Camera

LOG = logging.get_logger(__name__)


class Timelapsed(Camera):

    def __init__(self, argv):
        self.args = None
        self.frequency = None
        self.prefix = None
        self.delete = None
        self._hours_string = None
        self.hours = 'all'
        self.parse_args(argv)

        super(Timelapsed, self).__init__(config_dir=self.args.config_dir)

        LOG.info("Starting Timelapsed")
        self.setup()

    def setup(self):
        super(Timelapsed, self).setup()
        self.frequency = self.args.frequency if self.args.frequency else self.timelapse.get('frequency', 60)
        self.prefix = self.args.prefix if self.args.prefix else self.timelapse.get('prefix', None)
        self.delete = self.args.delete if self.args.delete else self.timelapse.get('delete', False)
        self._hours_string = self.args.hours if self.args.hours else self.timelapse.get('hours', 'all')
        self.hours = self._hours_string.split(',')
        LOG.info("Frequency set to %s seconds" % self.frequency)
        LOG.info("File prefix set to %s" % self.prefix)
        LOG.info("Local file delete is set to %s" % self.delete)
        LOG.info("Hours set to %s" % self._hours_string)

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
        parser.add_argument('--hours',
                            dest='hours',
                            help='Hours to run timelapse')

        self.args = parser.parse_args(args=argv)

    def get_pic(self):
        self.get_picture(name=self.prefix, use_timestamp=True)
        self.remote_save(delete_local=self.delete)

    def check_time(self):
        if self.hours == 'all':
            return True

        current_hour = datetime.now().hour
        if current_hour in self.hours:
            return True

        LOG.info("Current hour %i is not in the list of enabled hours" % datetime.now().hour)
        return False

    def run(self):
        if self.timelapse.get('enabled', False):
            while True:
                if self.check_time():
                    self.get_pic()
                    LOG.info("Sleeping for %s seconds..." % self.frequency)
                    time.sleep(float(self.frequency))
                else:
                    time.sleep(300)
        else:
            LOG.info('Timelapse is disabled.  Please review your config file.')


def main(argv=sys.argv[1:]):

    timelapsed = Timelapsed(argv)
    timelapsed.run()
