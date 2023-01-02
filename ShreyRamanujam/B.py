class numbers():
    def __init__(self, numbers):
        self.numbers = numbers

    def findtargetpairs(self, target):
        sno = 1
        targetdictionary = {}
        for i in range(0, len(self.numbers)):
            for j in range(0, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == target:
                    targetdictionary[sno] = [i, j]
                    sno += 1
        return targetdictionary


mynumbers = numbers([10, 20, 10, 40, 50, 60, 70])
target50 = mynumbers.findtargetpairs(50)
print(target50)
