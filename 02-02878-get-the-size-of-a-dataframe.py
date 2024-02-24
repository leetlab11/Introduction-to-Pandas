# popular
# df.shape[0] gives number of rows
# df.shape[1] gives number of columns
# df.size gives num_of_rows * num_of_cols

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
    return [players.shape[0], players.shape[1]]

#   OR    
#   df.shape gives a tuple (num_of_rows, num_of_cols)- so converted that to list

    return list(players.shape)

#   OR
#   len(df) gives number of rows, len(df.columns) give number of columns
  
    return [len(players), len(players.columns)]


# no companies listed
