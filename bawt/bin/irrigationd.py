import argparse
import sys
import threading
import time
from datetime import datetime

import bawt.log as logging
from bawt.subsystems.irrigation import Irrigation

LOG = logging.get_logger('irrigationd')
SLEEP = 10


class Irrigationd(Irrigation):

    def __init__(self, argv):
        self.args = None
        self.frequency = None
        self.prefix = None
        self.delete = None
        self._hours_string = None
        self.hours = 'all'
        self.parse_args(argv)

        super(Irrigationd, self).__init__()

        LOG.info("Starting Timelapsed")
        self.setup()

    def setup(self):
        #super(Irrigation, self).setup()
        self.frequency = self.args.frequency if self.args.frequency else self.irrigation.get('frequency', 60)
        self.prefix = self.args.prefix if self.args.prefix else self.irrigation.get('prefix', None)
        self.delete = self.args.delete if self.args.delete else self.irrigation.get('delete', False)
        self._hours_string = self.args.hours if self.args.hours else self.irrigation.get('hours', 'all')
        self.hours = self._hours_string.split(',')
        LOG.info("Frequency set to %s seconds" % self.frequency)
        LOG.info("File prefix set to %s" % self.prefix)
        LOG.info("Local file delete is set to %s" % self.delete)
        LOG.info("Hours set to %s" % self._hours_string)

    def parse_args(self, argv):

        parser = argparse.ArgumentParser(description='irrigation daemon')
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

    def run(self):
        LOG.info('Started irrigationd')
        current_time = datetime.datetime.now()
        for run in self.get_runs():
            print run
        LOG.debug("Sleeping for %i seconds" % SLEEP)
        time.sleep(SLEEP)

    def execute_defined_run(self, run_id):
        run = self._get_run_definition(run_id)
        run_time = run.get('run_time', None)
        run_zones = self._get_run_zones(run_id)
        jobs = []
        for zone in run_zones:
            thread = threading.Thread(target=self.timed_run(zone, run_time))
            jobs.append(thread)

        for job in jobs:
            job.start()

        for job in jobs:
            job.join()


def main(argv=sys.argv[1:]):

    irrigationd = Irrigationd(argv)
    irrigationd.run()
