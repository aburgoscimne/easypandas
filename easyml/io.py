import pandas as pd


@pd.api.extensions.register_dataframe_accessor("easy")
class _:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def save_df_to_parquet(self, dest_path: str, file_name: str):
        """
        Save pandas dataframe to a parquet file.
        """
        self._obj.to_parquet(
            f"{dest_path}/{file_name}",
            use_deprecated_int96_timestamps=True,
        )


def load_parquet_to_df(source_path: str, file_name: str) -> pd.DataFrame:
    """
    Load parquet file and returns a pandas dataframe.
    """
    return pd.read_parquet(f"{source_path}/{file_name}")
