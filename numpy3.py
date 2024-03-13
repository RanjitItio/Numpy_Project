#Calculate the Mean value from dataset and place in the Null value space
import numpy as np

arr = np.array([1,2, np.nan, 4, 5])

imputed_arr = np.where(np.isnan(arr), np.mean(arr[~np.isnan(arr)]), arr)

print(imputed_arr)
