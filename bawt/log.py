import logging
from logging.config import fileConfig
import sys

def get_logger(name, config):
    """
    Returns a new logger
    :param name: Logger name
    :return: Logger
    """
    fileConfig(config)
    log = logging.getLogger(name)
    return log
