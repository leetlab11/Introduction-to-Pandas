# this is basically unpivoting
# use pd.melt()
# use id_vars, var_name, value_name

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars = 'product', var_name = 'quarter', value_name = 'sales')

# no companies listed
