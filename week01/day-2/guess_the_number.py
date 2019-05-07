# Write a program that stores a number, and the user has to figure it out.

# The user can input guesses, after each guess the program would tell one

# of the following:

# The stored number is higher

# The stried number is lower

# You found the number: 8
answer = 8

guess = 0

while guess != answer:
 #   print("Please input your guess:")
    guess = int(input())

    if guess > answer:
        print("The stried number is lower")
    else:
        print("The stored number is higher")
print("You found the number: 8")
