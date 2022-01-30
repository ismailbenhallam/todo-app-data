"""Script to create a new todo and save it to the database"""

from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine

DB_STRING = "postgresql://tarik:pass@localhost/todo-db"
TABLE_NAME = "todos"
FOLDER = "./export"  # Folder in which we will generate the exported data


def main():
    # Create the connection to the database
    connection = create_engine(DB_STRING)

    # Prepare the todo to save
    dataframe = pd.DataFrame(
        {
            "title": ["Python learning"],
            "description": ["create a script to insert data to 'todos' table"],
            "state": [0],
            "priority": [1],
            "created_at": [datetime.now()],
        },
    )

    # save todo to the database
    dataframe.to_sql(
        TABLE_NAME,
        connection,
        if_exists="append",
        index=False,
    )

    # Close the connection
    connection.dispose()


if __name__ == "__main__":
    main()
