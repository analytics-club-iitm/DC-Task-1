import random
import math

y=[]
y1 = []
n = int(input("Enter dimension of vector"))
for i in range(0,n) :
    y1.append(random.random())
    y.append(random.choice([0,1]))

i=0
s=0
for i in range(0,n) :
    
    x=math.log(y1[i])
    z = math.log(1 - y1[i],2)
    s=s + y[i]*x+ (1 - y[i])*z
    
s = -s/n
print("The value of O is",s)
