import pandas as pd


@pd.api.extensions.register_series_accessor("easy")
class _:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def is_between(self, min_value, max_value):
        """
        Check if an attribute is inside a range.
        """
        return (self._obj >= min_value) & (self._obj <= max_value)

    def is_greater(self, reference):
        """
        Check if an attribute is greater than a reference value or another attribute.
        """
        return self._obj > reference

    def is_greater_or_equal(self, reference):
        """
        Check if an attribute is greater or equal than a reference value or another attribute.
        """
        return self._obj >= reference

    def is_less(self, reference):
        """
        Check if an attribute is less than a reference value or another attribute.
        """
        return self._obj < reference

    def is_less_or_equal(self, reference):
        """
        Check if an attribute is less or equal than a reference value or another attribute.
        """
        return self._obj <= reference
