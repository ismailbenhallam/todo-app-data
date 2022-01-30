"""Script to create a connection to 'todo-db' database"""

from sqlalchemy import create_engine

DB_STRING = "postgresql://tarik:pass@localhost/todo-db"

def get_connection():
    """Get a connection to 'todo-db' database"""
    
    connection = create_engine(DB_STRING)

    return connection
