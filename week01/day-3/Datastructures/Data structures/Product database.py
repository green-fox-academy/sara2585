map = {"Eggs": 200, "Milk": 200, "Fish": 400, "Apples": 150, "Bread": 50, "Chicken": 550}
#How much is the fish?
n = map["Fish"]
print(n)
#What is the most expensive product?
max = 0
for key in map:
    if max < map[key]:
        max = map[key]
print(max)

#What is the average price?
sum = 0
for key in map:
    sum += map[key]

len = len(map)
arg = sum/len
print(arg)

#How many products' price is below 300?

n =0
for key in map:
    if map[key] < 300:
        n += 1
print(n)
#Is there anything we can buy for exactly 125?

TF = False
for key in map:
    if map[key] == 125:
        TF = True
print(TF)

#What is the cheapest product?

min = map["Eggs"]
for key in map:
    if min > map[key]:
        min = map[key]
for key in map:
    if map[key] == min:
        print(key)

