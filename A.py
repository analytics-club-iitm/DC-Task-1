import random
import numpy as np

# Set the number of elements in the vectors
N = 100

# Create a vector of zeros and ones with N elements
y = np.random.randint(2, size=N)

# Create a vector of random numbers between [0, 1) with N elements
y_hat = np.random.random(N)

def cross_entropy_loss(y, y_hat):
    # Compute the cross-entropy loss
    loss = -(1/N) * np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
    return loss

loss = cross_entropy_loss(y, y_hat)
print(loss)