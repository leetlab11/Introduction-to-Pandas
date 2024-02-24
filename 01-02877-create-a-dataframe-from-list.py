# given list- student_data:
# [
#   [1, 15],
#   [2, 11],
#   [3, 11],
#   [4, 20]
# ]

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    df = pd.DataFrame(data = student_data, columns = ['student_id', 'age'])
    return df

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# same as above but concise
# first parameter in DataFrame() is always data, not need to mention as above
# columns parameter has name of columns in square brackets

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    return(pd.DataFrame(student_data, columns = ['student_id', 'age']))


# amazon- 3
# apple- 2
# adobe- 2
# google- 2
