"""Script to get all todos from the database"""

import pandas as pd
from sqlalchemy import create_engine

from constants import DB_STRING, TABLE_NAME


def get_todos_df(clauses=""):
    engine = create_engine(DB_STRING)

    # Load 'todos' to a DataFrame
    dataframe = pd.read_sql(f"SELECT * FROM {TABLE_NAME} {clauses}", engine)

    # Close the connection
    engine.dispose()

    return dataframe


if __name__ == "__main__":
    print(get_todos_df())
