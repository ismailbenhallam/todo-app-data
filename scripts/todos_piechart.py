"""Script to display a pie chart that shows todos status"""
import matplotlib.pyplot as plt

from todos_dataframe import get_todos_df


def main():
    labels = "Done", "Remaining"

    dataframe = get_todos_df()

    remainings_todos_count = len(dataframe[dataframe["state"] == 0])
    finished_todos_count = len(dataframe[dataframe["state"] != 0])

    sizes = [finished_todos_count, remainings_todos_count]

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Todos state")
    plt.show()


if __name__ == "__main__":
    main()
