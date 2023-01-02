import numpy as np
class target:
    def __init__(self,arr,tgtsum):
        self.arr = arr
        self.tgtsum = tgtsum
        self.dict = {}
        self.c = 1
    def pairs(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if self.arr[i] + self.arr[j] == self.tgtsum:
                    self.dict[self.c] = [i,j]
                    self.c += 1

        print(self.dict)
list = np.random.randint(0,100,25)
print(list)
s = target(list,50)
s.pairs()
