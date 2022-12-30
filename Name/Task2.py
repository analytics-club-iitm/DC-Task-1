class targetsum:
    def __init__(self,array,targetsum):
        self.array=array
        self.targetsum=targetsum
        self.dictionary={}
        self.ctr=0
    def show(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if(self.array[i]+self.array[j]==self.targetsum) and (i!=j):
                    self.dictionary[self.ctr+1]=[i,j]
                    self.ctr=self.ctr+1
        print(self.dictionary)
numbers=[10,20,10,40,50,60,70]
target=50
output=targetsum(numbers,target)
output.show()

