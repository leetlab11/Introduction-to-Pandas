# use concat()

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])

#   OR  
#   axis = 0 means concat rows
    return pd.concat([df1, df2], axis = 0)

# no companies listed
