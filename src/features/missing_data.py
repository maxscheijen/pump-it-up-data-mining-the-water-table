import numpy as np
from sklearn.impute import SimpleImputer


def replace_value_nan(df, columns, replaced_value=0):
    df[columns] = df[columns].replace(0, np.nan)
    return df


def fill_mean(df):
    num_cols = df.select_dtypes(['int', 'float']).columns
    df[num_cols] = (SimpleImputer(strategy='mean')
                    .fit_transform(df[num_cols]))
    return df


def fill_mode(df):
    cat_cols = df.select_dtypes(['O']).columns
    df[cat_cols] = (SimpleImputer(strategy='most_frequent')
                    .fit_transform(df[cat_cols]))
    return df
