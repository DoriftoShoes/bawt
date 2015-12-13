import logging
from logging.config import fileConfig
import sys

def setup(config='/home/pi/bawt/conf/logging.conf'):
    fileConfig(config, disable_existing_loggers=False)

def get_logger(name):
    """
    Returns a new logger
    :param name: Logger name
    :return: Logger
    """
    log = logging.getLogger(name)
    log.info("Created logger: %s" % name)
    return log
