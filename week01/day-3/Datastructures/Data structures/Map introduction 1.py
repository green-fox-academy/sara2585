dic = {}
n = len(dic)
print(n == 0)
dic = {97: "a", 98 : "b", 99: "c", 65: "A", 66: "B", 67: "C"}

#Print all the keys

for key in dic:
    print(key)
#Print all the values

for key in dic:
    print(dic[key])
#Add value D with the key 68
dic.update({68 : "D"})

#Print how many key-value pairs are in the map
n = len(dic)
print(n)

#Print the value that is associated with key 99
print(dic[99])

#Remove the key-value pair where with key 97

dic.pop(97)
#Print whether there is an associated value with key 100 or not

print(100 in dic)

#Remove all the key-value pairs
dic.clear()