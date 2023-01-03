class TaskB:
    def inp(self):
        self.n = list(map(int, input("Enter elements separated by a space and enter to finish\n").split()))
        self.target = int(input("Enter target sum value\n"))
        self.l = len(self.n)
    def calc(self):
        self.Dict = {}
        self.c = 1
        for i in range(self.l):
            for j in range(self.l):
                if(i==j):
                    continue
                if((self.n[i]+self.n[j]) == self.target):
                    self.Dict[self.c] = [i, j]
                    self.c = self.c + 1
    def output(self):
        print(self.Dict)

obj = TaskB()

obj.inp()
obj.calc()
obj.output()