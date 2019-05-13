class Animal():
    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst
        
    def eat(self):
         self.hunger -= 1
         return self.hunger

    def drink(self):
        self.thirst -= 1
        return self.thirst

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger, self.thirst

#tiger = Animal(10, 20)

#tiger_eat = tiger.eat()
#tiger_drink = tiger.drink()
#tiger_play = tiger.play()

#print(f"{tiger_eat}")
#print(f"{tiger_drink}")
#print(f"{tiger_play}")

