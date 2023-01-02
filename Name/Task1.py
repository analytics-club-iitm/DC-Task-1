import numpy as np
import math
arr1=np.random.rand(100)
arr2=np.random.randint(0,2,100)
sum=0
for i in range(100):
    sum=sum+(arr2[i]*(math.log(arr1[i],2))+(1-arr2[i])*(math.log(1-arr1[i],2)))
sum=-sum/100
print(sum)

