"""Script to get all todos from the database"""

import pandas as pd
from sqlalchemy import create_engine

TABLE_NAME = "todos"
DB_NAME = "todo-db"
DB_STRING = f"postgresql://tarik:pass@localhost/{DB_NAME}"


def get_todos_df(clauses=""):
    f"""Get all todos from the database"""

    # Get a connection to the database
    engine = create_engine(DB_STRING)

    # Load 'todos' to a DataFrame
    dataframe = pd.read_sql(f"SELECT * FROM {TABLE_NAME} {clauses}", engine)

    # Close the connection
    engine.dispose()

    return dataframe


if __name__ == "__main__":
    print(get_todos_df())
