import random
import math

y1 = [] # for floats - y^
y2 = [] # for 0s and 1s - y

for i in range(100):
    y1.append(random.random())
    y2.append(random.randint(0, 1))
sum = 0
for i in range(100):
    sum += y2[i]*math.log(y1[i], 2) + (1-y2[i])*math.log((1-y1[i]), 2)
sum = -sum/100
print(sum)