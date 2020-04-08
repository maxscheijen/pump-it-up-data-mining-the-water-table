import pandas as pd
from sklearn.preprocessing import LabelEncoder


def label_encoding(df: pd.DataFrame) -> pd.DataFrame:
    """Label encoding of categorical features.
    
    Parameters
    ----------
    df : pd.DataFrame
    
    Returns
    -------
    pd.DataFrame
        dataframe with categorical variables label encoded.
    """
    cat_cols = df.select_dtypes('O').columns.values
    df[cat_cols] = df[cat_cols].apply(LabelEncoder().fit_transform)
    return df
