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

        super(Irrigation, self).__init__()

        LOG.info("Starting Irrigationd")
        self.setup()

    def setup(self):
        pass

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
        while True:
            current_time = datetime.now()
            print self.irrigation
            for run_id, run_definition in self.get_runs().iteritems():
                print run_id
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
