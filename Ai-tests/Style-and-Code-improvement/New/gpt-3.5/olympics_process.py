"""
    Module for processing olympics data
"""

import pandas as pd


def read_data():
    """
    Read csv file and preprocess the data
    """
    # Read CSV file and skip the first row
    df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)

    # Rename columns
    columns = {}
    for col in df.columns:
        if col.startswith("№"):
            columns[col] = "#" + col.split()[1]
        elif col.startswith(("01", "02", "03")):
            parts = col.split(".")
            suffix = "." + parts[1] if len(parts) > 1 else ""
            medal_type = {"01 !": "Gold", "02 !": "Silver", "03 !": "Bronze"}[parts[0]]
            columns[col] = medal_type + suffix
    df.rename(columns=columns, inplace=True)

    # Split index into country name and ID
    df.index = df.index.str.split(r"\s\(").str[0]

    # Strip index values to remove leading/trailing whitespace
    df.index = df.index.str.strip()

    # Drop 'Totals' row
    df = df.drop("Totals")
    return df


def first_country(df):
    """
    Return Series of first country in df
    """
    return df.iloc[0]


def summer_biggest(df):
    """
    Return name of country that has won the biggest amount of medals at summer Olympics
    """
    return df["Total"].idxmax()


def difference_biggest(df):
    """
    Return country with the biggest difference between summer and winter golden medals number
    """
    return abs(df["Gold"] - df["Gold.1"]).idxmax()


def difference_biggest_relative(df):
    """
    Return name of country with the biggest relative gold medal count
    """
    df = df.loc[(df["Gold"] > 0) & (df["Gold.1"] > 0)]
    return (abs(df["Gold"] - df["Gold.1"]) / df["Gold.2"]).idxmax()


def get_points(df):
    """
    Add and return Points column
    """
    df["Points"] = 3 * df["Gold.2"] + 2 * df["Silver.2"] + df["Bronze.2"]
    return df["Points"]


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
