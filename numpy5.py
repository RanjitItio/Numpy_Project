#Calculate Percentile of a Given Data and clip the data between those two percentile
import numpy as np

arr = np.array([1, 2, 3, 100, 5, 6])

clipped_arr = np.clip(arr, np.percentile(arr, 1), np.percentile(arr, 99))


print(clipped_arr)
