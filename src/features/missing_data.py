import numpy as np
import pandas as pd
from typing import Union, List
from sklearn.impute import SimpleImputer


def replace_value_nan(df: pd.DataFrame, columns: List[str], replaced_value: Union[int, float]) -> pd.DataFrame: # noqa
    """Replace values with missing value indicator.

    Parameters
    ----------
    df : pd.DataFrame
    columns : List[str]
        list of columns in dataframe
    replaced_value : Union[int, float]
        value to replace with nan

    Returns
    -------
    pd.DataFrame
        Dataframe with missing values filled with nan
    """
    df[columns] = df[columns].replace(0, np.nan)
    return df


def fill_mean(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in numerical columns with mean.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Dataframe with missing numerical values filled with mean.
    """
    num_cols = df.select_dtypes(['int', 'float']).columns
    df[num_cols] = (SimpleImputer(strategy='mean')
                    .fit_transform(df[num_cols]))
    return df


def fill_mode(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in categorical columns with mode.
    
    Parameters
    ----------
    df : pd.DataFrame
    
    Returns
    -------
    pd.DataFrame
        Dataframe with missing categorical values filled with mode.
    """
    cat_cols = df.select_dtypes(['O']).columns
    df[cat_cols] = (SimpleImputer(strategy='most_frequent')
                    .fit_transform(df[cat_cols]))
    return df
