"""Script to export all todos from the database to JSON"""

import os

import emoji
from termcolor import colored

from helpers.todos_dataframe import get_todos_df

TABLE_NAME = "todos"
FOLDER = "./export"  # Folder in which we will generate the exported data


def export(folder: str = FOLDER):
    f"""Export all todos from the database to {folder}/{TABLE_NAME}.json"""

    dataframe = get_todos_df()

    # Create the folder for exported data
    if not os.path.exists(folder):
        os.mkdir(folder)

    # Export the todos to a JSON format
    dataframe.to_json(f"{folder}/{TABLE_NAME}.json", "records", indent=2, date_format="iso")

    JSON_FILE_PATH = os.path.abspath(f"{folder}/{TABLE_NAME}.json")

    print(
        colored(
            "\nYour todos have been exported to "
            + colored(JSON_FILE_PATH, attrs=["bold", "underline"])
            + " successfully ",
            "magenta",
        )
        + emoji.emojize(":grinning_face_with_big_eyes:")
        + "\n"
    )


if __name__ == "__main__":
    export()
