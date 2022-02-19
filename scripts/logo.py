from pyfiglet import Figlet
from termcolor import colored

from constants import APP_NAME

FONT = "standard"


def get_logo():
    f = Figlet(font=FONT)
    return colored(f.renderText(f">> {APP_NAME} <<"), "blue")


if __name__ == "__main__":
    print(get_logo())
