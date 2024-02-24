# df.head()- displays first few rows
# df.head(n)- displays first n rows
# df.tail()- displays last few rows
# df.tail(n)- displays last n rows

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
    return employees.head(3)


# no companies listed
