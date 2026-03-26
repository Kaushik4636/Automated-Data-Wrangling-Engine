import pandas as pd

class OutlierHandler:
    def __init__(self, method="iqr", factor=1.5):
        self.method = method
        self.factor = factor

    def fit(self, df):
        self.bounds = {}

        for col in df.select_dtypes(include=["int64", "float64"]).columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - self.factor * IQR
            upper = Q3 + self.factor * IQR

            self.bounds[col] = (lower, upper)

        return self

    def transform(self, df):
        df = df.copy()

        for col, (lower, upper) in self.bounds.items():
            df[col] = df[col].clip(lower, upper)

        return df

    def fit_transform(self, df):
        return self.fit(df).transform(df)