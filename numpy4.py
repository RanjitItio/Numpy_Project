#Caluculate Z_Score of a given data with standard deviation
#Find out Outlier(Deviation from Mean) from the data set
import numpy as np

data = np.array([1,2,8,4,5,15])

z_score = np.abs((data - np.mean(data)) / np.std(data))

is_outlier = z_score > 2
print(is_outlier)

cleaned_data = data[~is_outlier]

print(cleaned_data)
