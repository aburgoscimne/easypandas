import pandas as pd


def load_parquet_to_df(source_path: str, file_name: str) -> pd.DataFrame:
    """
    Load parquet file and returns a pandas dataframe.
    """
    return pd.read_parquet(f"{source_path}/{file_name}")


def save_df_to_parquet(df: pd.DataFrame, dest_path: str, file_name: str):
    """
    Save pandas dataframe to a parquet file.
    """
    df.to_parquet(
        f"{dest_path}/{file_name}",
        use_deprecated_int96_timestamps=True,
    )
