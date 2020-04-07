import pandas as pd


if __name__ == "__main__":
    # download data from DrivenData
    train_labels = pd.read_csv("https://s3.amazonaws.com/drivendata-prod/data/7/public/0bf8bc6e-30d0-4c50-956a-603fc693d966.csv") # noqa
    train_values = pd.read_csv("https://s3.amazonaws.com/drivendata-prod/data/7/public/4910797b-ee55-40a7-8668-10efd5c1b960.csv") # noqa

    # combine train label with train data
    raw_data = train_labels.merge(train_values, on='id')
    raw_data.to_csv("data/raw/raw_train_data.csv", index=None)
