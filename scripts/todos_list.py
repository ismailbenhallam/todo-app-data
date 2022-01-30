"""Script to display the remaining todos"""

import pandas as pd
from beautifultable import BeautifulTable
from termcolor import colored

from helpers.spinner import get_spinner
from helpers.todos_dataframe import get_todos_df

TABLE_NAME = "todos"

PRIORITY_PROPS_SWITCHER = {
    0: {"color": "red", "label": "High"},
    1: {"color": "yellow", "label": "Normal"},
    2: {"color": "white", "label": "Low"},
}


def main():
    f"""Display the remaining todos"""

    spinner = get_spinner()
    spinner.start()

    # Load 'todos' to a DataFrame
    dataframe = get_todos_df()

    # Prepare the table
    table = BeautifulTable()
    table.columns.header = list(
        map(lambda h: colored(h, "cyan"), ["ID", "Title", "Description", "Priority", "Creation date"])
    )

    # Insert todos into the table and show it
    for index, todo in dataframe.iterrows():
        priority = todo["priority"]

        table.rows.append(
            [
                todo["id"],
                todo["title"],
                todo["description"],
                colored(PRIORITY_PROPS_SWITCHER[priority]["label"], PRIORITY_PROPS_SWITCHER[priority]["color"]),
                str(todo["created_at"]),
            ]
        )

    spinner.stop()
    print("\n\n")
    print(table)
    print("\n\n")


if __name__ == "__main__":
    main()
