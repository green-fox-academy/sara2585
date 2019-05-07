# Write a program that reads a number from the standard input, then draws a

# triangle like this:

#

# *

# **

# ***

# ****

# The triangle should have as many lines as the number was
print("Please input a number of lines you want to print:")
a = 0
a = int(input())
J = 0
for i in range(a):
    for j in range(i):
        print ("*",end = '')
    print("*")
