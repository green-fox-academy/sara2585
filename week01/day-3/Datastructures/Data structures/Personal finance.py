list = [500, 1000, 1250, 175, 800, 120]
#How much did we spend?

sum = 0
for i in list:
    sum += i
print(sum)
#Which was our greatest expense?
max = 0
len = len(list)
for i in range(len):
    if max < list[i]:
        max = list[i]
print(max)



#Which was our cheapest spending?
min = list[0]
for i in range(len):
    if min > list[i]:
        min = list[i]
print(min)

#What was the average amount of our spendings?

arg = sum/len
print(arg)