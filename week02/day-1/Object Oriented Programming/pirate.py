import random

class Pirate:
    def __init__(self, name = pirate, n= 0, state = "alive"):
        self.name = name
        self.n = n
        self.state = state

    def drink_some_rum(self):
        if self.state != "alive":
            print("the pirate is died")
            return None
        else:
            self.n += 1
            return self.n
    def hows_it_going_mate(self, m = 0):
        for i in m:
            drink_some_rum()
        if self.n <= 4:
            print(f"Pour me anudder!")
        else:
            self.state = "pass out"
            print(f"Arghh, I'ma Pirate. How d'ya d'ink its goin?")
    def die(self, d=20):
        for i in range(20):
            drink_some_rum()
        if self.n == d:
            self.state = "die"
    def brawl(Pirate):
        if Pirate.state == "alive":
            i = random.randint(0, 2)
            if i == 0:
                self.state = "die"
            elif i == 1:
                Pirate.state = "die"
            else:
                self.state = "pass out"
                self.state = "pass out"

    




class Ship:
    def __init__(self, name = ship, r = 0):
        self.pirates = []
        self.name = name
        self.r = r

    def fill_ship(self, n = random.randint()):
        self.pirates.append(Pirate("captain"))
        for i in range(n-1):
            self.pirates.append(Pirate())

    def __str__(self):
        alivePirateCount = 0
        for pirate in self.pirate:
            if pirate.state == "alive":
                alivePirateCount += 1
        return f"The captain consumed {}"



    def battle(Ship):





    


        
