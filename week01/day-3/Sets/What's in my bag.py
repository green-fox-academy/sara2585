Oliver = {"Laptop", "Notebook", "Pen", "Sunglasses", "Hand sanitizer"}
Ethen = {"Sunglasses", "Notebook", "Phone"}
Mia = {"Laptop", "Sunglasses", "Hand sanitizer"}

#What are the common items in Oliver's and Ethan's bag?

OandE = Oliver & Ethen
print(OandE)
#What are the items that in Oliver's bag but not in Mia's bag?

OM = Oliver - Mia
print(OM)
#What are the common items in Oliver's, Ethan's and Mia's bag?

OEM = set.union(Oliver, Ethen, Mia)
print(OEM)