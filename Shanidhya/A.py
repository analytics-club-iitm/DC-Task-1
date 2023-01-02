import math
import random

n = 100
O = 0
y = [None] * 100
yhat = [None] * 100

for i in range(n):
    x = random.random()
    if (x < 0.5):
        y[i] = 0
    else:
        y[i] = 1

for i in range(n):
    yhat[i] = random.random()

for i in range(n):
    O += (-1/n)*(y[i]*math.log2(yhat[i]) + (1-y[i])*math.log2(1-yhat[i]))

print(O)
