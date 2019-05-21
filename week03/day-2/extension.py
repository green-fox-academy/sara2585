def add(a, b):
    return a + b

def max_of_three(a, b, c):
    max = 0
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return  b
    else:
        return c

def median(pool):
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    teve_list = []
    for char in teve:
        teve_list.append(char)
    for i in range(len(teve_list)):
        if is_vovel(teve_list[i]):
            teve_list[i] = teve_list[i] + "v" + teve_list[i]
    return "".join(teve_list)

#print(translate("hungaa"))