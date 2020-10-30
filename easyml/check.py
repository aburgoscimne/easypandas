import pandas as pd


@pd.api.extensions.register_dataframe_accessor("check")
class _:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def get_sorted_columns(
        self, column_list: list = None, ascending: bool = True
    ) -> list():
        """
        Returns a list of given columns sorted by their mean values.
        """
        if column_list is None:
            column_list = self._df.columns.to_list()

        sorted_column_list = list()
        for _ in range(0, len(column_list)):
            minimum = 0
            for j in range(1, len(column_list)):
                if (
                    self._df[column_list[j]] < self._df[column_list[minimum]]
                ).mean() > 0.5:
                    minimum = j
            sorted_column_list.append(column_list[minimum])
            column_list.pop(minimum)

        if ascending:
            return sorted_column_list

        return sorted_column_list[::-1]


@pd.api.extensions.register_series_accessor("check")
class _:
    def __init__(self, pandas_obj):
        self._series = pandas_obj

    def is_between(self, min_value, max_value):
        """
        Check if an attribute is inside a range.
        """
        return (self._series >= min_value) & (self._series <= max_value)

    def is_greater(self, reference):
        """
        Check if an attribute is greater than a reference value or another attribute.
        """
        return self._series > reference

    def is_greater_or_equal(self, reference):
        """
        Check if an attribute is greater or equal than a reference value or another attribute.
        """
        return self._series >= reference

    def is_less(self, reference):
        """
        Check if an attribute is less than a reference value or another attribute.
        """
        return self._series < reference

    def is_less_or_equal(self, reference):
        """
        Check if an attribute is less or equal than a reference value or another attribute.
        """
        return self._series <= reference
