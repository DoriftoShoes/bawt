from switchboard.board import Board
import yaml

class Bawt(object):

    DEFAULT_DIRECTORY = 'tmp'
    DEFAULT_RESOLUTION = { 'x': 1024,
                           'y': 768 }
    def __init__(self):
        self.board = Board()
        self.config = yaml.safe_load(open('conf/main.yaml'))

        self.subsystems = self.config.get('subsystems', None)
        for subsystem, config in self.subsystems.iteritems():
            if config.get('enabled', False):
                try:
                    conf_file = self.config.get('config', None)
                    if conf_file:
                        conf_file_path = conf_file
                    else:
                        conf_file_path = "conf/%s.yaml" % subsystem
                    conf = yaml.safe_load(open(conf_file_path))
                    setattr(self, subsystem, conf)
                except Exception as e:
                    print("Could not activate %s subsystem.  Error: %s" % (subsystem, str(e)))

        self.aws = self.config.get('aws', None)
