"""
    US popualation analysis
"""

import pandas as pd


def read_data(path_to_file):
    """
    Return DataFrame of population data from path_to_file
    >>> read_data("census.csv")
    """
    return pd.read_csv(path_to_file)


def max_counties(df):
    """
    Return name of state with biggest amount of counties
    >>> max_counties(read_data("census.csv"))
    """
    return df.groupby("STNAME").size().idxmax()


def max_difference(df):
    """
    Return county with greatest population estimete change
    >>> max_difference(read_data("census.csv"))
    """
    df = df.loc[df["STNAME"] != df["CTYNAME"]]
    differences = abs(
        df.loc[:, "POPESTIMATE2010":"POPESTIMATE2015"].max(axis=1)
        - df.loc[:, "POPESTIMATE2010":"POPESTIMATE2015"].min(axis=1)
    )
    return df.loc[differences.idxmax(), "CTYNAME"]


def conditional_counties(df):
    """
    Return counties from region 1 or 2 with name staring from
    Washington and POPESTIMATE2015 is greater POPESTIMATE2014
    >>> conditional_counties(read_data("census.csv"))
    """
    df = df.loc[
        df["REGION"].isin([1, 2])
        & df["CTYNAME"].str.startswith("Washington")
        & (df["POPESTIMATE2015"] > df["POPESTIMATE2014"])
    ]
    return df.loc[:, ["STNAME", "CTYNAME"]]


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
