"""Script to create a connection to 'todo-db' database"""

from sqlalchemy import create_engine
from termcolor import colored

DB_NAME = "todo-db"
DB_STRING = f"postgresql://tarik:pass@localhost/{DB_NAME}"


def get_connection():
    """Get a connection to 'todo-db' database"""

    connection = create_engine(DB_STRING)

    return connection


if __name__ == "__main__":
    print(
        colored(
            f"\nThis script provides a function to create a connection to '{DB_NAME}' database\n"
            "It cannot be run directly\n",
            "yellow",
        )
    )
