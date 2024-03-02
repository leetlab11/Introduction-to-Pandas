# subset parameter- we need to provide a list of columns based on which duplicates are determined

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ['email'])

#    OR
#    keep parameter has 3 values- first, last, False-
#    'first' keeps 1st duplicate values and removes the rest 
#    'last' keeps last duplicate values and removes the rest 
#    'False' removes all duplicate values
    return customers.drop_duplicates(subset = ['email'], keep = 'first')

# no companies listed
