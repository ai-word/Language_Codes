import pandas as pd
import numpy as np
# read from
data = pd.read_csv('stu.csv')
print(data)

# save to
data.to_pickle('student.pickle')


