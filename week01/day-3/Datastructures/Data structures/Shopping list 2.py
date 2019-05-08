price = {"Milk": 1.07, "Rice": 1.59, "Eggs": 3.14, "Cheese": 12.60, "Chicken Breasts": 9.40, "Apples": 2.31, "Tomato": 2.58, "Potato": 1.75, "Onion": 1.10}
Bob = {"Milk": 3, "Rice": 2, "Eggs": 2, "Cheese": 1, "Chicken Breasts": 4, "Apples": 1, "Tomato": 2, "Potato": 1 }
Alice = {"Rice": 1, "Eggs": 5, "Chicken Breasts": 2, "Apples": 1, "Tomato": 10}
#How much does Bob pay?

Bobpay = 0

for key in Bob:
    amount = Bob[key] * price[key]
    Bobpay += amount
print(Bobpay)
    
#How much does Alice pay?
Alicepay = 0
for key in Alice:
    amount = Alice[key] * price[key]
    Alicepay += amount
print(Alicepay)

#Who buys more Rice?
if "Rice" in Bob:
    BobRice = Bob["Rice"]
else:
    BobRice = 0

if "Rice" in Alice:
    AliceRice = Alice["Rice"]
else:
    AliceTice = 0

if BobRice > AliceRice:
    print("Bob")
elif BobRice == AliceRice:
    print("The same")
else:
    print("Alice")

##Who buys more Potato?
if "Potato" in Bob:
    BobP = Bob["Potato"]
else:
    BobP = 0
if "Potato" in Alice:
    AliceP = Alice["Potato"]
else:
    AliceP = 0

if BobP > AliceP:
    print("Bob")
elif BobP == AliceP:
    print("The same")
else:
    print("Alice")
#Who buys more different products?

Bobnum = len(Bob)
Alicenum = len(Alice)

if Bobnum > Alicenum:
    print("Bob")
elif Bobnum == Alicenum:
    print("the same")
else:
    print("Alice")
#Who buys more products? (piece)
Bobitems = 0
for key in Bob:
    Bobitems += Bob[key]

Aliceitems = 0
for key in Alice:
    Aliceitems += Alice[key]
if Bobitems > Aliceitems:
    print("Bob")
elif Bobitems == Aliceitems:
    print("The same")
else:
    print("Alice")
