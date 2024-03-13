#Delete the rows or columns from the data which are blank

import numpy as np

arr = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])

arr_missing_value = np.delete(arr, np.where(np.isnan(arr).any(axis=1)), axis=0)

print(arr_missing_value)


