def count_ears(n):
    if n == 0:
        return n
    else:
        return 2 + count_ears(n-1)
