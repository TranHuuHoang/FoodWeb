import pandas as pd


def percentage(string, df):
    n = df.shape[0]
    row_count = df[df['text'].str.contains(string, case=False)].shape[0]
    percentage = row_count/n * 100
    return percentage