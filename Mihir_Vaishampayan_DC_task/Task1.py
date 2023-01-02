import numpy as np
import math
import random

cross_entr=0

list1=[]
list2=[]
for i in range(0,100,1):
    list1.append(random.randint(0,1))

for i in range(0,100,1):
    list2.append(random.randint(0, 9999)/10000)

y=np.array(list1)
y2=np.array(list2)

for i in range(0,100,1):
    cross_entr=cross_entr+y[i]*math.log(y2[i],2)
    cross_entr=cross_entr+(1-y[i])*math.log((1-y2[i]), 2)

cross_entr=-cross_entr/100

print(cross_entr)