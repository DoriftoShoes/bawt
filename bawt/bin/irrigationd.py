import argparse
import sys
import threading
import time
from datetime import datetime

import bawt.log as logging
from bawt.subsystems.irrigation import Irrigation

LOG = logging.get_logger('irrigationd')


class Irrigationd(Irrigation):

    def __init__(self, argv):
        self.parse_args(argv)

        super(Irrigation, self).__init__(config_dir=self.args.config_dir)
        self.args = None
        self.irrigationd_config = self.irrigation.get('irrigationd')
        self.sleep = None

        LOG.info("Starting Irrigationd")
        self.setup()

    def setup(self):
        self.sleep = self.args.sleep if self.args.sleep else self.irrigationd_config.get('sleep', 30)

    def parse_args(self, argv):

        parser = argparse.ArgumentParser(description='irrigation daemon')
        parser.add_argument('--config-dir',
                            dest='config_dir',
                            default='conf/main.yaml',
                            help='path to the config file')
        parser.add_argument('--sleep',
                            dest='frequency',
                            help='Frequency of capture')

        self.args = parser.parse_args(args=argv)

    def run(self):
        while True:
            self.read_config(self.args.config_dir)
            current_time = datetime.now().strftime('%H:%M')
            for run_id, run_definition in self.get_runs().iteritems():
                start_time = run_definition.get('start_time', None)
                if start_time == current_time:
                    self.execute_defined_run(run_id)
                else:
                    LOG.info("Current time %s does not match start time %s for run: %i" %
                             (current_time, start_time, run_id))
            LOG.info("Sleeping for %i seconds" % self.sleep)
            time.sleep(self.sleep)

    def execute_defined_run(self, run_id):
        run = self.get_run_definition(run_id)
        if not self.is_run_enabled(run_id):
            LOG.info("Run: %i is currently disabled.  Skipping." % run_id)
            return False

        run_time = run.get('run_time', None)
        run_zones = self.get_run_zones(run_id)
        jobs = []
        for zone in run_zones:
            if not self.is_zone_enabled(zone):
                LOG.info("Zone %i is in run %i but it is disabled.  Skipping." % (zone, run_id))
                continue

            LOG.info("Queueing zone: %i for run" % zone)
            thread = threading.Thread(target=self.timed_run(zone, run_time))
            jobs.append(thread)

        for job in jobs:
            job.start()

        for job in jobs:
            job.join()


def main(argv=sys.argv[1:]):

    irrigationd = Irrigationd(argv)
    irrigationd.run()
