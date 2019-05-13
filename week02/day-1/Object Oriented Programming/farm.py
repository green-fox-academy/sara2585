from Animal import Animal
class Farm():
    def __init__(self, slots = 4):
        self.animals = []
        self.animals.append(Animal(20, 30))
        self.animals.append(Animal(50, 50))
        self.animals.append(Animal(80, 60))
        self.animals.append(Animal(45, 70))
        self.slots = slots

    def breed(self):
        n = len(self.animals)
        if n < self.slots:
            for i in range(0, self.slots-n):
                self.animals.append(Animal())
        return self.animals

    def slaughter(self):
        min_hungry = self.animals[0]
        for i in self.animals:
            if i.hunger < min_hungry.hunger:
                min_hungry = i
        self.animals.remove(min_hungry)
        return self.animals

farm = Farm()
farm.breed()
print(farm.animals)
farm.slaughter()
print(farm.animals)
            
