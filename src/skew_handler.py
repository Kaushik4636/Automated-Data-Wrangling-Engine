import pandas as pd
import numpy as np

class SkewHandler:
    def __init__(self, method="log", threshold=0.5):
        self.method = method
        self.threshold = threshold
        self.skewed_cols = []

    def fit(self, df):
        self.skewed_cols = []
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

        for col in numeric_cols:
            skewness = df[col].skew()
            if abs(skewness) > self.threshold:
                self.skewed_cols.append(col)

        return self

    def transform(self, df):
        df = df.copy()
        for col in self.skewed_cols:
            if self.method == "log":
                df[col] = df[col].apply(lambda x: np.log1p(x))
            elif self.method == "sqrt":
                df[col] = df[col].apply(lambda x: np.sqrt(x))
        return df

    def fit_transform(self, df):
        return self.fit(df).transform(df)