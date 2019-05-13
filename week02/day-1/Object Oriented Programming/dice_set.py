import random



class DiceSet(object):



    def __init__(self):

        self.dices = [0, 0, 0, 0, 0, 0]



    def roll(self):

        for i in range(len(self.dices)):

            self.dices[i] = random.randint(1, 6)

        return self.dices



    def get_current(self, index = None):

        if index != None:

            return self.dices[index]

        else:

            return self.dices



    def reroll(self, index = None):

        if index != None:

            self.dices[index] = random.randint(1, 6)

        else:

            self.roll()





dice_set = DiceSet()
dice_set.roll()

for i in range(0,len(dice_set.dices)):
    while dice_set.dices[i] != 6:
        dice_set.reroll(i)
        dice_set.get_current(i)

print(dice_set.dices)




#print(dice_set.get_current())

#dice_set.roll()

#print(dice_set.get_current())

#dice_set.reroll(3)

#print(dice_set.get_current(3))

#print(dice_set.get_current())

