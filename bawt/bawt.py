
import yaml

from switchboard.board import Board
import log as logging

class Bawt(object):

    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = {'x': 1024,
                          'y': 768}

    def __init__(self, config_dir='conf/'):

        config_file = "%s/main.yaml" % config_dir
        self.board = Board()
        self.config = yaml.safe_load(open(config_file))
        self.logging_config = self.config.get('logging', None).get('config_file', None)
        self.logger = logging.get_logger(__name__, self.logging_config)

        self.subsystems = self.config.get('subsystems', None)
        for subsystem, config in self.subsystems.iteritems():
            if config.get('enabled', False):
                try:
                    conf_file = self.config.get('config', None)
                    if conf_file:
                        conf_file_path = conf_file
                    else:
                        conf_file_path = "%s/%s.yaml" % (config_dir, subsystem)
                    conf = yaml.safe_load(open(conf_file_path))
                    setattr(self, subsystem, conf)
                    self.logger.info("Initializing subsystem: %s" % subsystem)
                except Exception as e:
                    self.logger.info("Could not activate %s subsystem.  Error: %s" % (subsystem, str(e)))

        self.aws = self.config.get('aws', None)

