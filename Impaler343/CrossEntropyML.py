import numpy as np
import math 

n = 100

y_=np.random.rand(100,)
y=np.random.randint(0,2,(100,))

exp = -(sum([y[i]*math.log(y_[i],2)+(1-y[i])*math.log(1-y_[i],2) for i in range(n)]))/n

print(exp)
