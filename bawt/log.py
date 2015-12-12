import logging
from logging.config import fileConfig
import sys

def exception_handler(type, value, tb):
    logger.exception("Uncaught exception: {0}".format(str(value)))

def get_logger(name, config):
    """
    Returns a new logger
    :param name: Logger name
    :return: Logger
    """
    sys.excepthook = exception_handler
    fileConfig(config)
    log = logging.getLogger(name)
    return log
