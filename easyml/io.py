import pathlib
from typing import Union
import pandas as pd


@pd.api.extensions.register_dataframe_accessor("io")
class _:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def save(
        self,
        path: Union[str, pathlib.Path],
        saving_format: str = "parquet",
        *args,
        **kwargs,
    ):
        """
        Saves pandas dataframe to a file. It can be in
        parquet or csv format.
        Write object to a comma-separated values (csv) file.

        Parameters
        ----------
        path : str or file handle, default None
            File path or object where the dataframe has to be saved.

        format : str, default "parquet"
            The way the dataframe has to be saved.
        """
        assert saving_format in [
            "parquet",
            "csv",
        ], "saving_format has to be parquet or csv."

        if saving_format == "parquet":
            self._df.to_parquet(path, *args, **kwargs)
        elif saving_format == "csv":
            self._df.to_csv(path, *args, **kwargs)


def load(path: Union[str, pathlib.Path]) -> pd.DataFrame:
    """
    Load parquet or csv file and returns a pandas dataframe.
    Files to load must be on parquet or csv format.

    Parameters
        ----------
        path : str or file handle, default None
            File path or object where the source file is.
    """

    try:
        return pd.read_parquet(path)
    except OSError:
        try:
            return pd.read_csv(path)
        except:
            raise ValueError("Bad parsing specs or not a parquet nor csv file.")
