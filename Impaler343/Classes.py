class Indices:
    def __init__(self,l,t):
        self.d={}
        self.ct=1
        self.l=l
        self.t=t

    def calc(self):
        n=len(self.l)
        for i in range(n-1):
            for j in range(i+1,n):
                if self.l[i]+self.l[j]==self.t:
                    self.d[self.ct]=(i,j)
                    self.d[self.ct+1]=(j,i)
                    self.ct+=2
        return self.d

numbers = [int(i) for i in input().split()]
target = int(input())
Soln = Indices(numbers, target)
print(Soln.calc())

