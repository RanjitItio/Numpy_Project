#Convert an 1D Array to 2D Array with 2 Rows
import numpy as np

arr = np.arange(10)
# arr = np.array([1,2,3,4,5,6,7,8,9,10])

array = arr.reshape(2, -1)

print(array)
