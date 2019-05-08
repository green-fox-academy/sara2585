#Create a list ('List A') which contains the following values 
A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
#Apple, Avocado, Blueberries, Durian, Lychee
#Create a new list ('List B') with the values of List A
B = A.copy()

#Print out whether List A contains Durian or not

print("Durian" in A)
#Remove Durian from List B

B.remove("Durian")
#Add Kiwifruit to List A after the 4th element

A.insert(4, "Kiwifruit")
print(A)
#Compare the size of List A and List B

a = len(A)
b = len(B)

#Get the index of Avocado from List A

A.index("Avocado")
#Get the index of Durian from List B

B.index("Durian")
#Add Passion Fruit and Pummelo to List B in a single statement

B.extend(["Passion", "Fruit", "Pummelo"])
#Print out the 3rd element from List A

print(A[2])