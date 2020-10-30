import pandas as pd
import numpy as np


@pd.api.extensions.register_dataframe_accessor("clean")
class _:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def drop_na_or_constant_columns(self) -> pd.DataFrame:
        """
        Delete those columns that are null or constant.
        """
        return self._df.loc[:, self._df.nunique(dropna=False) != 1]

    def drop_na_rows(self) -> pd.DataFrame:
        """
        Delete those rows which values are all null.
        """
        return self._df.dropna(axis="rows", how="all")

    def drop_columns(self, column_names: list) -> pd.DataFrame:
        """
        Delete listed columns.
        """
        return self._df.drop(columns=column_names, errors="ignore")


@pd.api.extensions.register_series_accessor("clean")
class _:
    def __init__(self, pandas_obj):
        self._series = pandas_obj

    def zero_as_na(self) -> pd.Series:
        """
        Delete those values that are 0, since it represents a missing value.
        """
        return self._series.replace(0, np.nan)
