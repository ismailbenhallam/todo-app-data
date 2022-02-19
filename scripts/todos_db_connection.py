"""Script to get a connection to the database"""

from sqlalchemy import create_engine

from constants import DB_STRING
from logger import get_logger


def get_connection():
    # Get a connection to the database
    return create_engine(DB_STRING)


if __name__ == "__main__":
    log = get_logger(__name__)
    log.error("This is a script to get a connection to the DB")
