from functools import reduce
numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]


even_numbers = list(filter(lambda x: x % 2 ==0 and x <= 10, numbers))
sum_even_numbers = reduce(lambda a, b: a+b, even_numbers)
print(sum_even_numbers)