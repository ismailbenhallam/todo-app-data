"""Script to export todos table to JSON"""

import os

import pandas as pd

from todo_connection import get_connection

TABLE_NAME = "todos"
FOLDER = "./export"  # Folder in which we will generate the exported data


def main():
    f"""Export the 'todos' from the database to {FOLDER}/{TABLE_NAME}.json"""

    # Get a connection to the database
    engine = get_connection()

    # Load 'todos' to a DataFrame
    dataframe = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)

    # Create the folder for exported data
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    # Export the todos to a JSON format
    dataframe.to_json(f"{FOLDER}/{TABLE_NAME}.json", "records", indent=2, date_format="iso")
    print(f"'todos' table entries exported to {FOLDER}/{TABLE_NAME}.json")

    # Close the connection
    engine.dispose()


if __name__ == "__main__":
    main()
