import numpy as np
import math as m
import random as r
arr1 = np.array([]) 
# arr1 is the vector y
arr = np.array([])
# arr is the vector y cap
choice = (0,1)
O = 0
n = int(input('Enter the number of dimensions:'))
for i in range(n):
    arr = np.append(arr,r.random()) # random numbers in the range [0,1)
    arr1 = np.append(arr1,r.choice(choice)) # 0s and 1s
    O += arr1[i]*m.log2(arr[i]) + (1-arr1[i])*m.log2(1 - arr[i])
O /= -n
print(O) # Cross Entropy





