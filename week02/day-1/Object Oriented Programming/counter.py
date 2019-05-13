class Counter():
    def __init__(self, num = 0, tmp =0):
        self.num = num
        self.tmp = num

    def add(self, num1= 1):
        self.num += num1
        return self.num

    def get(self):
        return self.num

    def reset(self):
        self.num = self.tmp
        return self.num



#counter = Counter(4)
#add = counter.add()
#get = counter.get()
#reset = counter.reset()
#print(f'{add}')
#print(f'{get}')
#print(f'{reset}')



    