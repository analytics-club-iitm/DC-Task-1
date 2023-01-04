import numpy as np
n=100
ycap=np.random.rand(n)
y=np.random.randint(0,2,n)
def cross_entropy_loss(y,ycap):
    O = -np.sum((np.multiply(y,np.log2(ycap))+np.multiply(1-y,np.log2(1-ycap))))/n
    return O

print(cross_entropy_loss(y,ycap))
