class Target():
    def __init__(self, ar, targ):
        self.ar = ar
        self.targ = targ
        self.d = dict()
    def sumcheck(self):
        a = self.ar
        count = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if (a[i] + a[j] == self.targ):
                    count += 1
                    self.d[count] = [i,j]
        return self.d

a = eval(input("Enter an array of numbers: "))
t = int(input("Enter target sum: "))

c = Target(a, t)
print(c.sumcheck())