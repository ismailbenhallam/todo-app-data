"""Script to display the remaining todos"""

from logo import get_logo
from spinner import get_spinner
from todos_table import get_table


def main():
    f"""Display the remaining todos"""

    print(get_logo())

    spinner = get_spinner()
    spinner.start()

    table = get_table(
        ["title", "description", "priority", "created_at"],
        "WHERE state = 0 ORDER BY priority, state",
    )

    spinner.hide()
    spinner.stop()
    print(table)


if __name__ == "__main__":
    main()
