import math
import numpy as np

y = np.random.randint(0,2,100)
ycap = np.random.rand(100)

n=100
S=0
for i in range(100):
    S += (y[i]*math.log(ycap[i],2) + (1-y[i])*math.log(1-ycap[i],2))

print("The Cross-Entropy loss",-S/n)

