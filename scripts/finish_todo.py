import emoji
import inquirer
from inquirer.themes import GreenPassion

from constants import TABLE_NAME
from logger import get_logger
from todos_dataframe import get_todos_df
from todos_db_connection import get_connection


def finish_todo():
    df = get_todos_df("where state = 0")
    todos = []
    for index, todo in df.iterrows():
        todos.append({"id": todo["id"], "title": todo["title"], "description": todo["description"]})

    print("\n")
    question = inquirer.List("todos", message="Choose a todo to set as 'done'", choices=list(map(__print_todo, todos)))
    answers = inquirer.prompt([question], theme=GreenPassion())

    if answers == None:
        exit()

    choosen_id = str(answers["todos"]).split(":")[0]

    log = get_logger(__name__)
    engine = get_connection()

    engine.execute(f"UPDATE {TABLE_NAME} SET state = 1 WHERE id = '{choosen_id}'")

    engine.dispose()
    log.info("Done " + emoji.emojize(":grinning_face_with_big_eyes:"))


def __print_todo(todo):
    desc = todo["description"]
    return f"{todo['id']}: {todo['title']} ({desc})" if desc else f"{todo['id']}: {todo['title']}"


if __name__ == "__main__":
    finish_todo()
