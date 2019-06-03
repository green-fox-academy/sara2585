numbers = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

positive_numbers = list(filter(lambda n: n > 0, numbers))

squared_positives = list(map(lambda x: x **2, positive_numbers))
print(squared_positives)


