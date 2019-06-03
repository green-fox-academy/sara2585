numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

contains_even_numbers = any(list(map(lambda x: x % 2 ==0, numbers)))
print(contains_even_numbers)