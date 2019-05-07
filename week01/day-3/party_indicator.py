# Write a program that asks for two numbers

# The first number represents the number of girls that comes to a party, the

# second the boys

# It should print: The party is exellent!

# If the the number of girls and boys are equal and there are more people coming than 20

#

# It should print: Quite cool party!

# It there are more than 20 people coming but the girl - boy ratio is not 1-1

#

# It should print: Average party...

# If there are less people coming than 20

print("Please input the number of girls:")
girls = int(input())
print("Please input the number of boys:")
boys = int(input())
if girls == boys:
    print("The party is exellent!")
elif(girls + boys) > 20:
    print("Quite cool party!")
else:
    print("Average party...")
