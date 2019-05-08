
# - Create a function called `factorio`

#   that returns it's input's factorial
def factorio(n):
    fact = 1
    if n < 0:
        print("need a positive number")
    elif n == 0:
        print("0's factorial is 0" )
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact
print(factorio(3))
