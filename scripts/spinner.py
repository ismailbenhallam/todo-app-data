import time

from termcolor import colored
from yaspin import yaspin


def get_spinner():
    spinner = yaspin().moon
    spinner.text = "Loading..."
    return spinner


if __name__ == "__main__":
    print(
        colored(
            f"\nThis script provides a function to create a spinner (like the one showed bellow)"
            "\nIt cannot be run directly\n",
            "yellow",
        )
    )
    spinner = get_spinner()
    spinner.start()
    time.sleep(5)
    spinner.stop()
