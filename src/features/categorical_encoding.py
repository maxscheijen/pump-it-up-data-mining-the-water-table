from sklearn.preprocessing import LabelEncoder


def label_encoding(df):
    cat_cols = df.select_dtypes('O').columns.values
    df[cat_cols] = df[cat_cols].apply(LabelEncoder().fit_transform)
    return df