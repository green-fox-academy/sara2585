# - Create a variable named `p1`

#   with the following content: `[1, 2, 3]`

# - Create a variable named `p2`

#   with the following content: `[4, 5]`

# - Print "p2 is longer" if `p2` has more elements than `p1`
p1 = [1, 2, 3]
p2 = [4, 5]
lenp1 = len(p1)
lenp2 = len(p2)
if lenp1 < lenp2:
    print("p2 is longer")
elif lenp1 == lenp2:
    print("They are same long" )
else:
    print("P1 is longer")
