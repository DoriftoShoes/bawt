import logging
from logging.config import fileConfig

import yaml

from switchboard.board import Board


class Bawt(object):

    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = {'x': 1024,
                          'y': 768}

    def __init__(self, config_dir='conf/'):

        config_file = "%s/main.yaml" % config_dir
        self.board = Board()
        self.config = yaml.safe_load(open(config_file))
        self.logging_config = self.config.get('logging', None).get('config_file', None)
        self.log = self.get_logger(__name__)

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
                    self.log.info("Initializing subsystem: %s" % subsystem)
                except Exception as e:
                    self.log.info("Could not activate %s subsystem.  Error: %s" % (subsystem, str(e)))

        self.aws = self.config.get('aws', None)

    def get_logger(self, name):
        """
        Returns a new logger
        :param name: Logger name
        :return: Logger
        """
        fileConfig(self.logging_config)
        log = logging.getLogger(name)
        log.debug("Logger initialized.")
        return log
