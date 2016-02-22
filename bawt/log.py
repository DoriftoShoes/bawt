import logging
from logging.config import fileConfig


def setup(config='/home/pi/bawt/conf/logging.conf'):
    fileConfig(config, disable_existing_loggers=False)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.propagate = False


def get_logger(name):
    """
    Returns a new logger
    :param name: Logger name
    :return: Logger
    """
    log = logging.getLogger(name)
    log.info("Created logger: %s" % name)
    return log
