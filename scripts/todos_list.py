"""Script to display the remaining todos"""

from beautifultable import BeautifulTable
from termcolor import colored

from spinner import get_spinner
from todos_dataframe import get_todos_df

TABLE_NAME = "todos"

PRIORITY_PROPS_SWITCHER = {
    0: {"color": "red", "label": "High", "state": "Doing"},
    1: {"color": "yellow", "label": "Normal", "state": "Done"},
    2: {"color": "white", "label": "Low", "state": "Canceled"},
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
        map(lambda h: colored(h, "cyan"), ["Title", "Description", "Priority", "State", "Creation date"])
    )

    # Insert todos into the table and show it
    for index, todo in dataframe.iterrows():
        priority = todo["priority"]

        table.rows.append(
            [
                todo["title"],
                todo["description"],
                colored(PRIORITY_PROPS_SWITCHER[priority]["label"], PRIORITY_PROPS_SWITCHER[priority]["color"]),
                PRIORITY_PROPS_SWITCHER[todo["state"]]["state"],
                todo["created_at"].strftime("%d %b %Y %H:%M:%S"),
            ]
        )

    spinner.hide()
    spinner.stop()
    print(table)


if __name__ == "__main__":
    main()
