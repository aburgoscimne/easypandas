import pandas as pd


@pd.api.extensions.register_dataframe_accessor("io")
class _:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def save_to_parquet(self, dest_path: str, file_name: str):
        """
        Save pandas dataframe to a parquet file.
        """
        self._df.to_parquet(
            f"{dest_path}/{file_name}",
            use_deprecated_int96_timestamps=True,
        )


def load_from_parquet(source_path: str, file_name: str) -> pd.DataFrame:
    """
    Load parquet file and returns a pandas dataframe.
    """
    return pd.read_parquet(f"{source_path}/{file_name}")
