class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.pairs = {}
        self.count = 0
    
    def find_pairs(self):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    self.count += 1
                    self.pairs[self.count] = [i, j]
        return self.pairs

# Example usage
finder = PairFinder([10,20,10,40,50,60,70], 50)
print(finder.find_pairs())
# Output: {1: [0, 3], 2: [2, 3], 3: [3, 0], 4: [3, 2]}