import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][['name', 'age']]

#   OR
#   more popular
#   df.loc[]- always square brackets after 'loc'- loc stands for location 
    return students.loc[students['student_id'] == 101, ['name', 'age']]

#   OR
    return students.loc[students['student_id'] == 101][['name', 'age']]

#   OR
#   name: means pull all columns after name
    return students.loc[students['student_id'] == 101, 'name':]

#  OR
    return students.loc[students.student_id == 101, 'name':]

 

# no companies listed
