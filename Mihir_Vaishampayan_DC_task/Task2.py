
class pair_search:
    key=0
    leng=0
    index=1
    arr=[]
    dict={}
    def getdata(self):
        print("Enter the key")
        self.key=int(input())
        print("Enter the elements of array")
        self.arr=list(map(int, input().split()))
        self.leng=len(self.arr)
    def count(self):
        for i in range(0,self.leng,1):
            for j in range(0, self.leng, 1):
                if(self.arr[i]+self.arr[j]==self.key):
                    self.dict[self.index]=[i, j]
                    self.index=self.index+1
        
        
C1=pair_search()
C1.getdata()
C1.count()
print(C1.dict)
