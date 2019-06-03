numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))

average_value = sum(odd_numbers)/len(odd_numbers)
print(average_value)
