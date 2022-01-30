"""Inquire 'Todo' from console"""

from email.policy import default

from inquirer import List, Text, errors, prompt
from inquirer.themes import GreenPassion
from termcolor import colored

TITLE_MIN_CHARS = 3


def __validate_title(answers, title):
    if len(title) < TITLE_MIN_CHARS:
        raise errors.ValidationError("", f"Title should be {TITLE_MIN_CHARS} chars at least")
    return True


def get_todo_answers():
    questions = [
        Text("title", message=colored("Please enter todo title", "green"), validate=__validate_title),
        Text("description", message=colored("Please enter todo description", "green")),
        List(
            "priority",
            message=colored("Please enter priority", "green"),
            choices=[["NORMAL", 1], ["HIGH", 0], ["LOW", 2]],
            default=1,
        ),
    ]
    answers = prompt(questions, theme=GreenPassion())
    return answers


if __name__ == "__main__":
    print(get_todo_answers())
