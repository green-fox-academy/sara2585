# Crate a program that draws a chess table like this

#

# % % % % 

#  % % % %

# % % % %

#  % % % %

# % % % %

#  % % % %

# % % % % 

#  % % % %

print("Please input a number:")
n = int(input())
for i in range(n):
    if i % 2 == 0:
        print(" % % % %")
    else:
        print("% % % %")