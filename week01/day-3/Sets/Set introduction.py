#Create a set
#Add at least 5 members to the set
sets1 = {1, 3, 5, 7, 7, 482}

#Remove at most 2 members from the set
sets1.discard(3)
sets1.discard(1)

#Iterate over the set and print its members
for i in sets1:
    print(i)

#Remove 482 from the set if it is present
sets1.discard(482)

#Remove 42 from the set even if it is not present
sets1.discard(42)

print(sets1)