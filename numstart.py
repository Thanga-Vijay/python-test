# import numpy as np

# a = np.array([1, 2, 3, 4])
# x = a.view()
# a[0] = 32

# print(a)
# print(x)

# #print(type(ar))
# # import numpy as np

# # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# # print(arr)

import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print(a)
