"""
Module for processing population data of counties
"""

import pandas as pd

def read_data(path_to_file):
    """
    Return DataFrame of population data from path_to_file
    """
    return pd.read_csv(path_to_file)


def max_counties(df):
    """
    Return name of state with the biggest amount of counties
    """
    return df['STNAME'].value_counts().idxmax()


def max_difference(df):
    """
    Return county with the greatest population estimate change
    """
    population_columns = [
        f'POPESTIMATE{i}' for i in range(2010, 2016)
    ]
    df['POPULATION_CHANGE'] = (
        df[population_columns].max(axis=1) - df[population_columns].min(axis=1)
    )
    filtered_df = df[df['STNAME'] != df['CTYNAME']]
    max_change_index = filtered_df['POPULATION_CHANGE'].idxmax()
    return filtered_df.loc[max_change_index, 'CTYNAME']


def conditional_counties(df):
    """
    Return counties from region 1 or 2 with names starting from Washington 
    and POPESTIMATE2015 greater than POPESTIMATE2014
    """
    condition = (
        df['REGION'].isin([1, 2]) &
        df['CTYNAME'].str.startswith("Washington") &
        (df['POPESTIMATE2015'] > df["POPESTIMATE2014"])
    )
    return df.loc[condition, ['STNAME', 'CTYNAME']]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
