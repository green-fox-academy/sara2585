numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

sum_even_numbers = sum(list(filter(lambda x: x % 2 ==0 and x <= 10, numbers)))
print(sum_even_numbers)