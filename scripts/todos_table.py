"""Script to display the remaining todos"""

import datetime

from beautifultable import BeautifulTable
from termcolor import colored

from logger import get_logger
from todos_dataframe import get_todos_df

PRIORITY_PROPS_SWITCHER = {
    0: {
        "label": "High",
        "state": "Doing",
        "color": "red",
    },
    1: {
        "label": "Normal",
        "state": "Done",
        "color": "yellow",
    },
    2: {
        "label": "Low",
        "state": "Canceled",
        "color": "white",
    },
}


def header_to_todo_column(todo, header):
    value = todo[header]

    if header == "state":
        return PRIORITY_PROPS_SWITCHER[value]["state"]

    if header == "priority":
        return colored(PRIORITY_PROPS_SWITCHER[value]["label"], PRIORITY_PROPS_SWITCHER[value]["color"])

    if isinstance(value, datetime.date):
        return value.strftime("%d %b %Y %H:%M:%S")

    return value


def todo_to_row(todo, columns_header):
    return list(map(lambda header: header_to_todo_column(todo, header), columns_header))


def get_table(columns_header: list, clause: str = ""):
    f"""Get a beautiful table of todos"""

    # Load 'todos' to a DataFrame

    # "ORDER BY priority, state"
    dataframe = get_todos_df(clause)

    # Prepare the table
    table = BeautifulTable()
    table.columns.header = list(
        map(lambda h: colored(h, "cyan"), list(map(lambda header: str(header).title(), columns_header)))
    )

    # Insert todos into the table and show it
    for index, todo in dataframe.iterrows():
        table.rows.append(todo_to_row(todo, columns_header))

    return table


if __name__ == "__main__":
    log = get_logger(__name__)
    log.error("This is a util script to draw a table")
