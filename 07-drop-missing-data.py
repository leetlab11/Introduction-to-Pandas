# subset parameter- we need to provide a list of columns based on which na values are determined

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ['name'])

# parameter 'axis' has values 0 and 1
# 0- row is to be removed
# 1- col is to be removed

# parameter 'how' has values 'any' and 'all
# any- if from the subset list, if any value is null, that row/col is removed
# all- if from the subset list, if all value is null, that row/col is removed

# no companies listed
