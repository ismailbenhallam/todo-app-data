"""Script to create a new todo and save it to the database"""

from datetime import datetime

import emoji
import pandas as pd
from sqlalchemy import create_engine
from termcolor import colored

from inquire_todo import get_todo_answers

DB_STRING = "postgresql://tarik:pass@localhost/todo-db"
TABLE_NAME = "todos"
FOLDER = "./export"  # Folder in which we will generate the exported data


def main():

    todo = get_todo_answers()
    if not todo:
        exit(0)

    # Create the connection to the database
    connection = create_engine(DB_STRING)

    # Prepare the todo to save
    dataframe = pd.DataFrame(
        {
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
    print(colored("Todo saved successfully ", color="magenta") + emoji.emojize(":grinning_face_with_big_eyes:") + "\n")

    # Close the connection
    connection.dispose()


if __name__ == "__main__":
    main()