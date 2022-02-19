import logging

import coloredlogs

LOG_LEVEL = "INFO"


def get_logger(name: str):
    logger = logging.getLogger(name)
    coloredlogs.install(level=LOG_LEVEL, logger=logger)
    return logger
