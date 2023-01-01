import math
import random

n = 100
a=[]
b=[]

for i in range(100):
    a.append(random.random())
    b.append(random.randint(0,1))

print(a,"\n",b)
sum=0
for i in range(100):
    sum= sum + ((b[i])*math.log2(a[i]))+((1-b[i])*(1-math.log2(1-a[i])))

print("\n The value of the expresssion is",sum)







