import log as logging
import yaml
from switchboard.board import Board

LOG = logging.get_logger(__name__)


class Bawt(object):

    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = {'x': 1024,
                          'y': 768}

    def __init__(self, config_dir='conf/'):
        self.config = None
        self.subsystems = None
        self.aws = None
        self.weather = None

        self.board = Board()
        self.read_config(config_dir)
        self.logging_config = self.config.get('logging', None).get('config_file', None)
        logging.setup(self.logging_config)

    def read_config(self, config_dir):
        config_file = "%s/main.yaml" % config_dir
        self.config = yaml.safe_load(open(config_file))
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
                except Exception as e:
                    LOG.critical("Could load subsystem config: %s.  Error: %s" % (subsystem, str(e)))

        self.aws = self.config.get('aws', None)
        weather_source = self.config.get('weather', None).get('source', None)
        self.weather = self.config.get('weather', None).get(weather_source, None)