from pandas import DataFrame

"""
all the mapping to types should be in side in this file
"""
from typing import List


def obj_2_dataframe(lines: List) -> DataFrame:
    results = list(map(lambda x: x.as_dict(), lines))
    return DataFrame(results)
