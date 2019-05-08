map = {"Eggs": 200, "Milk": 200, "Fish": 400, "Apples": 150, "Bread": 50, "Chicken": 550}
#Which products cost less than 201? (just the name)

for key in map:
    if map[key] < 201:
        print(key)

#Which products cost more than 150? (name + price)

for key in map:
    if map[key] > 150:
        print(f"{key}  {map[key]}")