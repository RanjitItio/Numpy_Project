#Below Numpy program will check for any blank data in the given data set and fill the blank
#Data with some specified data

import numpy as np

data = np.array([1, 2, np.nan, 4, 5])
print(data)

has_missing = np.isnan(data)

print(has_missing)

# data[has_missing] = 0 
arr_filled = np.nan_to_num(data)

print(arr_filled)
