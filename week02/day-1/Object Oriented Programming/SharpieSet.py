from Sharpie import Sharpie
class SharpieSet():
    def __init__(self):
        self.sets = []
        self.sets.append(Sharpie("white", 2.0, 0))
        self.sets.append(Sharpie("black", 12.0, 100))
        self.sets.append(Sharpie("pink", 10.0, 200))
        self.sets.append(Sharpie("green", 3.0, 0))
    def count_useable(self, count = 0):
        for i in range(0, len(self.sets)):
            if self.sets[i].ink_amount > 0:
                count += 1
        return count
    def remove_trash(self):
        for i in self.sets:
            if i.ink_amount == 0:
                self.sets.remove(i)
        return self.sets

sharpeiesets = SharpieSet()
print(sharpeiesets.count_useable())
print(sharpeiesets.remove_trash())
    
