from missing_handler import MissingValueHandler
from outlier_handler import OutlierHandler
from skew_handler import SkewHandler

class DataWranglingPipeline:
    def __init__(self, missing_strategy="mean", outlier_method="iqr", skew_method="log"):
        self.missing_handler = MissingValueHandler(strategy_num=missing_strategy)
        self.outlier_handler = OutlierHandler(method=outlier_method)
        self.skew_handler = SkewHandler(method=skew_method)

    def fit(self, df):
        df_clean = self.missing_handler.fit_transform(df)
        df_clean = self.outlier_handler.fit_transform(df_clean)
        df_clean = self.skew_handler.fit_transform(df_clean)
        return df_clean

    def fit_transform(self, df):
        return self.fit(df)