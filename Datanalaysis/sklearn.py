from sklearn import preprocessing
import numpy as np
import pandas as pd
x_array = np.array([2,3,5,6,7,4,8,7,6])
normalized_arr = preprocessing.normalize([x_array])
print(normalized_arr)