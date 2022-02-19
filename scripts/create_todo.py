"""Script to create a new todo and save it to the database"""

import uuid
from datetime import datetime

import emoji
import pandas as pd
from sqlalchemy import create_engine

from constants import DB_STRING, TABLE_NAME
from inquire_todo import get_todo_answers
from logger import get_logger
from spinner import get_spinner


def main():

    # Get todo details from console
    todo = get_todo_answers()
    if not todo:
        exit(0)

    # Show a spinner while trying to save todo in the database
    spinner = get_spinner()
    spinner.start()

    # Create the connection to the database
    connection = create_engine(DB_STRING)

    # Prepare todo to save
    dataframe = pd.DataFrame(
        {
            "id": [uuid.uuid4()],
            "title": [todo["title"]],
            "description": [todo["description"]],
            "priority": [todo["priority"]],
            "created_at": [datetime.now()],
            "state": 0,
        },
    )

    # Save todo to the database
    dataframe.to_sql(
        TABLE_NAME,
        connection,
        if_exists="append",
        index=False,
    )

    spinner.stop()

    log = get_logger(__name__)
    log.info("Todo saved successfully " + emoji.emojize(":grinning_face_with_big_eyes:"))

    # Close the connection
    connection.dispose()


if __name__ == "__main__":
    main()
