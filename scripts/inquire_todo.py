"""Inquire 'Todo' from console"""

from inquirer import List, Text, errors, prompt
from inquirer.themes import GreenPassion
from termcolor import colored

TITLE_MIN_CHARS = 3


def __validate_title(answers, title):
    if len(title) < TITLE_MIN_CHARS:
        raise errors.ValidationError("", f"Title should be {TITLE_MIN_CHARS} chars at least")
    return True


def get_todo_answers():
    print(colored("\n>>> Please enter todo details\n", "cyan"))
    questions = [
        Text("title", message=colored("Title", "green"), validate=__validate_title),
        Text("description", message=colored("Description", "green")),
        List(
            "priority",
            message=colored("Priority", "green"),
            choices=[["Normal", 1], ["High", 0], ["Low", 2]],
            default=1,
        ),
    ]
    answers = prompt(questions, theme=GreenPassion())
    return answers


if __name__ == "__main__":
    print(get_todo_answers())
