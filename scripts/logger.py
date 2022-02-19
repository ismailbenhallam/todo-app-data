import logging

import coloredlogs

LOG_LEVEL = "INFO"


def get_logger(name: str):
    logger = logging.getLogger(name)
    coloredlogs.install(level=LOG_LEVEL, logger=logger)
    return logger


if __name__ == "__main__":
    log = get_logger(__name__)
    log.error("This is a script to get a logger to use in other scripts")
