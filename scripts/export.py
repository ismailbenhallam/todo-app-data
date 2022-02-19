"""Script to export all todos from the database to JSON"""

import argparse
import os

import emoji
from termcolor import colored

from constants import EXPORT_FOLDER, TABLE_NAME
from todos_dataframe import get_todos_df

EXTENSION = ".json"


def export(folder: str = EXPORT_FOLDER, filename: str = TABLE_NAME):
    f"""Export all todos from the database to {folder}/{TABLE_NAME}{EXTENSION}"""

    json_file_path = os.path.abspath(f"{folder}/{filename}{EXTENSION}")

    # Get data from DB
    dataframe = get_todos_df()

    # Create the folder for exported data
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Export the todos to a JSON format
    dataframe.to_json(json_file_path, "records", indent=2, date_format="iso")

    print(
        colored(
            "\nYour todos have been exported to "
            + colored(json_file_path, attrs=["bold", "underline"])
            + " successfully ",
            "magenta",
        )
        + emoji.emojize(":grinning_face_with_big_eyes:")
        + "\n"
    )

    return json_file_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to export all todos from the database to JSON")
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory in which you wich to save the exported data",
        required=False,
        default=EXPORT_FOLDER,
    )
    parser.add_argument(
        "-f",
        "--filename",
        help="File name in which you wich to save the exported data (without extension)",
        required=False,
        default=f"{TABLE_NAME}",
    )
    args = vars(parser.parse_args())

    export(args.get("directory"), args.get("filename"))
