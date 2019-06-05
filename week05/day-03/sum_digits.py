def sum_digit(n):
    if n % 10 == n:
        return n
    else:
        return n % 10 + sum_digit(n // 10)
