def count_ears(n):
    if n == 0:
        return 0
    elif n ==1:
        return 2
    elif n % 2 ==0:
        return 3 + count_ears(n-1)
    else:
        return 2 + count_ears(n-1)
