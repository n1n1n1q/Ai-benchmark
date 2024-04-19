"""
    Module for processing olympics data
"""
import pandas as pd


def read_data():
    """
    Read csv file
    """
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0]
    df['ID'] = names_ids.str[1].str[:3]

    df = df.drop('Totals')

    return df


def first_country(df):
    """
    Return Series of dirst country in df
    >>> first_country(read_data())
    """
    return df.iloc[0]


def summer_biggest(df):
    """
    Return name of country that has won biggest amount of medals at
    summer olympics
    >>> summer_biggest(read_data())
    """
    return df.sort_values(by=['Total'], ascending=False).iloc[0].name



def difference_biggest(df):
    """
    Return country with biggest difference between summer and winter 
    golden medals number
    >>> difference_biggest(read_data())
    """
    return abs(df['Gold'] - df['Gold.1']).idxmax()


def difference_biggest_relative(df):
    """
    Return name of country with biggest relative gold medal count
    >>> difference_biggest_relative(read_data())
    """
    df = df.loc[(df["Gold"]>0) & (df["Gold.1"]>0)]
    return (abs(df['Gold'] - df['Gold.1']) / df['Gold.2']).idxmax()


def get_points(df):
    """
    Add and return Points column
    >>> get_points(read_data())
    """
    df["Points"] = 3 * df["Gold.2"] + 2 * df["Silver.2"] + df['Bronze.2']
    return df["Points"]



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
