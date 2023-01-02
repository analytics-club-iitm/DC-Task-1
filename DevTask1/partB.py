class partB():
    def __init__(self, list, target):
        self.nlist = list
        self.dict = {}
        self.count = 0
        self.target = target
    def find(self):
        for i in range(0, len(self.nlist)):
            for j in range(0, len(self.nlist)):
                if self.nlist[i] + self.nlist[j] == self.target:
                    self.dict[self.count] = [i, j]
                    self.count += 1
        print(self.dict)

x = partB([10,20,10,40,50,60,70], 50)
x.find()