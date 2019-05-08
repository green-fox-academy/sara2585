map = {"978-1-60309-452-8": "A Letter to Jo", "978-1-60309-459-7": "Lupus", "978-1-60309-444-3": "Red Panda and Moon Bear", "978-1-60309-461-0": "The Lab"}
for key in map:
    print(f"{map[key]} (ISBN: {key})")

#Remove the key-value pair with key 978-1-60309-444-3
map.pop("978-1-60309-444-3")


#Remove the key-value pair with value The Lab
key1 = ""
for key in map:
    if map[key] == "The Lab":
        key1 = key
map.pop(key1)





#Add the following key-value pairs to the map

map.update({"978-1-60309-450-4": "They Called Us Enemy", "978-1-60309-453-5": "Why Did We Trust Him?"})

#Print whether there is an associated value with key 478-0-61159-424-8 or not

print("478-0-61159-424-8" in map)
#Print the value associated with key 978-1-60309-453-5

print(map["978-1-60309-453-5"])