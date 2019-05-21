class mySum:
    def __init__(self, numlist = []):
        self.numlist = numlist

    def Sum(self):
        sum = 0
        for num in self.numlist:
            sum += num
        return sum


