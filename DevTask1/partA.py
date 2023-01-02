import numpy as np
import math
num = 100
ycap = np.random.rand(num)
ycap1 = 1 - ycap
y = np.random.randint(0,2,(num))
y1 = 1 - y
sum = 0
for i in range(0,num):
    sum = sum + y[i]*(math.log(ycap[i],2)) + y1[i]*(math.log(ycap1[i],2))
O = (-1)*sum/num
print(O)