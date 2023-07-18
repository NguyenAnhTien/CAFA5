"""
@author : Tien Nguyen
@date   : 2023-06-02
"""
from typing import Dict, List, Union

import pandas

def read_csv(
        sep: str,
        csv_file: str
    ) -> pandas.DataFrame:
    df = pandas.read_csv(csv_file, sep=sep, engine='python')
    return df

def create_df(
        df: Union[Dict, List[Dict]]
    ) -> pandas.DataFrame:
    """
    @desc:
        - Create pandas.DataFrame from dict or list of dict
    """
    return pandas.DataFrame(df)

def write_csv(
        df, 
        csv_file, 
        sorted=False, 
        by=None
    ) -> None:
    """
    @args:
        - df       : pandas.DataFrame
        - csv_file : str
        - sorted   : boolean
        - by       : list of strings or string
    @desc:
        - Write pandas.DataFrame to csv file
    """
    df = create_df(df)
    if sorted:
        df = df.sort_values(by=by, ascending=False)
    df.to_csv(csv_file, index=False)

def create_series(
        data: list
    ) -> pandas.Series:
    return pandas.Series(data)
