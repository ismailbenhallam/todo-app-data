"""Script to drop all TODOs from the DB"""

import inquirer

from constants import TABLE_NAME
from logger import get_logger
from logo import get_logo
from todos_db_connection import get_connection


def delete_all():
    engine = get_connection()

    engine.execute(f"DELETE FROM {TABLE_NAME}")


if __name__ == "__main__":
    print(get_logo())
    answers = inquirer.prompt(
        [inquirer.Confirm("confirm", message="You are about deleting all TODOs from the DB. Are you sure ?")],
    )

    if answers["confirm"]:
        delete_all()
        log = get_logger(__name__)
        log.info("All TODOs where deleted")
