import numpy as np
n = 100
y_cap = np.random.rand(n)
y = np.random.randint(0, 2, n)
O = -np.mean(y*np.log2(y_cap)+(1-y)*np.log2(1-y_cap))
print("Cross Entropy loss function value is ",O)

