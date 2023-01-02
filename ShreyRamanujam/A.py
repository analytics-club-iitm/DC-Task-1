import random
import math
y1 = []
y2 = []  # Same as y cap
for i in range(100):
    y1.append(random.randint(0,1))
    y2.append(random.uniform(0,1))
o = 0
for i in range(100):
    o += y1[i] * math.log2(y2[i]) + (1 - y1[i]) * math.log2(1-y2[i])

o = -o/100
print("Cross-Entropy loss value is: ", o)
