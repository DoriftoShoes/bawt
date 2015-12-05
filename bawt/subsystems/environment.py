from bawt.bawt import Bawt

class Environment(Bawt):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.sensors = self.environment.get('sensors', None)
        self.logger.info(__name__)
