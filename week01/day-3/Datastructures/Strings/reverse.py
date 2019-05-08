
# Create a function called 'reverse' which takes a string as a parameter

# The function reverses it and returns with the reversed string

def reverse(str):
    list_str = list(str)
    n = len(list_str)
    for i in range(0, int(n/2)):
        list_str[i],list_str[-(i+1)] = (list_str[-(i+1)], list_str[i] )
    str = "".join(list_str)
    return(str)



reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

print(reverse(reversed))