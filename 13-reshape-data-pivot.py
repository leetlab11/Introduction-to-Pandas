# use pivot- use index, columns and values parameters

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')

# no companies listed
