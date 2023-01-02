import numpy as np
import math
vec1 = np.random.rand(100)
vec2 = np.random.randint(0,2,100)
n = 100
sum = 0
for i in range(100):
    sum = sum + (vec2[i] * math.log(vec1[i],2) + (1 - vec2[i]) * math.log(1 - vec1[i],2))

print(-sum/n)
