from matplotlib import pyplot as plt  
import numpy as np 
# Samples random values from standard normal distribution (Size = 100)
noise = np.random.randn(100)
# Create a lin-spaced array x with 100 elements
x = np.linspace(-10,10,100)
y = 3*x + noise
plt.plot(x,y)
plt.show()