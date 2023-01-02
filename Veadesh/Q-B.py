class FindPair:
    def __init__(self,array,target):
        self.array = array
        self.target = target
        self.dict = {}
        self.key = 1

    def show(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if(self.array[i]+self.array[j]==self.target):
                    self.dict[self.key] = [i,j]
                    self.key += 1

        print(self.dict)


numbers= [10,20,10,40,50,60,70]
target=50
find=FindPair(numbers,target)
find.show()

