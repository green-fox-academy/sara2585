def greatest_common_divisor(n, m):
    if n > m:
        n, m = m, n
    if n % m == 0:
        return m
    else:
        return greatest_common_divisor(n, m%n)

print(greatest_common_divisor(12, 6))
