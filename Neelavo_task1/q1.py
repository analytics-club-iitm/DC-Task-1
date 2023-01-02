import random
import math
n=100
sum1=0
yc=[]
y=[]
for i in range(0,n,1):
    yc.append(random.random())
    y.append(random.randint(0,1))
    sum1=sum1+(y[i]*math.log(yc[i],2)+ (1-y[i])*math.log(1-yc[i],2))

O=-1*(sum1/n)

print(O)



  
