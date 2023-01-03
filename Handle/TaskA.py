import random
import math

bala_JEE = int(input("input bro:"))
lis = []
lis2 = []
 
for i in range(bala_JEE):
    lis.append(random.random())

    lis2.append(random.randint(0,1))

x = 0

for i in range(bala_JEE):
    x = x + lis2[i]*math.log(lis[i],2)+(1-lis2[i])*math.log(1-lis[i],2)

print((-1)*x/bala_JEE)