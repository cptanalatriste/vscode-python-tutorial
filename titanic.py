import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name: str = "titanic3.csv"


def main() -> None:
    data_frame: pd.DataFrame = pd.read_csv(file_name)

    figure, axis = plt.subplots(ncols=2, figsize=(30, 5))
    sns.violinplot(
        x="survived", y="age", hue="sex", data=data_frame, ax=axis[0]
    )
    sns.violinplot(
        x="survived", y="fare", hue="sex", data=data_frame, ax=axis[1]
    )
    plt.show()


if __name__ == "__main__":
    main()
