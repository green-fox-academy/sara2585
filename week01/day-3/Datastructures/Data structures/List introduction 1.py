list = []
n = len(list)
print(n)
list.append("William")
print(len(list) == 0)
list.append("John")
list.append("Amanda")
n1 = len(list)
print(n1)
print(list[2])

for i in list:
    print(i)

list.remove("John")

for i in range(2):
    print(list[-(i+1)])

list.clear()