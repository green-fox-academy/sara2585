def number_adder(n):
    if n == 0:
        return n
    else:
        return n + number_adder(n-1)
