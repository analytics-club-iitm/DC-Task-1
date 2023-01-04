import random
import math

n = 100

y = [random.randint(0,1) for _ in range(n)]
y_hat = [random.random() for _ in range(n)]

loss = 0
for i in range(n):
    loss += y[i]*math.log(y_hat[i], 2) + (1-y[i])*math.log(1-y_hat[i],2)

print(f'Loss = {loss}')