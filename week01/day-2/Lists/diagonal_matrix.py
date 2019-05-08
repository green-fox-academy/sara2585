
# - Create (dynamically) a two dimensional list

#   with the following matrix. Use a loop!

#

#   1 0 0 0

#   0 1 0 0

#   0 0 1 0

#   0 0 0 1

#

# - Print this two dimensional list to the output
a = [1, 0, 0, 0]
print (a)
for i in range(0, 3):
    a[i], a[i+1] = (a[i+1], a[i])
    print(a)
        