# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0
def Division(n = 10):
    
    try:
        m = int(input("Please input the division number:"))
        result = n / m
        print(result)
    except ZeroDivisionError:
        print("fail")

    except ValueError:
        print("Please input a integer")

division = Division()


