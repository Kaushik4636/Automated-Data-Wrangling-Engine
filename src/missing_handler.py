import pandas as pd

class MissingValueHandler:
    def __init__(self, strategy_num="mean", strategy_cat="mode"):
        self.strategy_num = strategy_num
        self.strategy_cat = strategy_cat

    def fit(self, df):
        self.fill_values = {}

        for col in df.columns:
            if df[col].dtype in ["int64", "float64"]:
                if self.strategy_num == "mean":
                    self.fill_values[col] = df[col].mean()
                elif self.strategy_num == "median":
                    self.fill_values[col] = df[col].median()
            else:
                self.fill_values[col] = df[col].mode()[0]

        return self

    def transform(self, df):
        df = df.copy()
        for col, value in self.fill_values.items():
        # Replace missing values without inplace
           df[col] = df[col].fillna(value)
        return df
    def fit_transform(self, df):
        return self.fit(df).transform(df)