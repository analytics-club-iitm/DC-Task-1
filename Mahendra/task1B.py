class sumpairs:
    def __init__(self, l, target):
        self.l=l
        self.target=target
        self.d={}
    
    def findpairs(self):
        for i in range(len(self.l)):
            for j in range(len(self.l)):
                if self.l[i]+self.l[j]==self.target:
                    self.d[len(self.d)+1]=[i,j]
        return self.d

#test:
a=sumpairs([10,20,10,40,50,60,70],50)
print(a.findpairs())
