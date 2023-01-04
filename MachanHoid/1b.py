class Solve:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.result = {}

    def findpairs(self):
        k = 1
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    self.result[k] = [i,j]
                    k += 1
#example
prob = Solve([10,20,10,40,50,60,70], 50)
prob.findpairs()
print(prob.result)

#user input
numbers = list(map(float, input("enter numbers: ").split()))
target = float(input("enter target: "))
prob2 = Solve(numbers, target)
prob2.findpairs()
print(prob2.result)