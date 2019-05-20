import abc
class Sweet:
    @abc.abstractclassmethod
    def __init__(self, type, price, sugaramount):
        pass
class Lollipop(Sweet): 
    def __init__(self, type = "lollipop", price = 10, sugaramount= 5):
        self.type = type
        self.price = price
        self.sugaramount = sugaramount

class Candie(Sweet):
    def __init__(self, type = "candie", price = 20, sugaramount = 10):
        self.type = type
        self.price = price
        self.sugaramount = sugaramount

class Candyshop:
    def __init__(self, sugar, income, inventory = []):
        self.sugar = sugar
        self.income = income
        self.inventory = inventory

    def createSeet(self, sweet):
        self.inventory.append(sweet)
        self.sugar -= sweet.sugaramount

    def raiseprice(self, amount):
        for i in self.inventory:
            i.price += amount


    def sell(self, amount, type):
        for i in range(amount):
            for sugar in self.inventory:
                if sugar.type == type:
                    self.income += sugar.price
                    self.inventory.remove(sugar)
              
    def buySugar(self, amount):
        if amount <= self.income:
            self.sugar += amount/100*1000
            self.income -= amount

    def toString(self):
        candies = 0
        lollipops = 0
        for i in self.inventory:
            if i.type == "candie":
                candies += 1
            else:
                lollipops += 1
        return f"Inventory: {candies} candies, {lollipops} lollipops, Income: {self.income}, Sugar: {self.sugar}g"

candie1 = Candie()
candie2 = Candie()
lollipop1 = Lollipop()

candyshop = Candyshop(1000,500)
candyshop.createSeet(candie1)
candyshop.createSeet(candie2)
candyshop.createSeet(lollipop1)

print(candyshop.sugar)

candyshop.raiseprice(2)

candyshop.sell(1, "candie")
for i in candyshop.inventory:
    print(i.price)
print(candyshop.income)

candyshop.buySugar(100)
print(candyshop.income)
print(candyshop.sugar)
print(candyshop.toString())









