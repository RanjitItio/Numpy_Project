import numpy as np
import pandas as pd

train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')

# train.info()

#Check Datatype, Rows and Columns in a File
print("The train data has", train.shape)
print("The train data has", test.shape)

train.head()