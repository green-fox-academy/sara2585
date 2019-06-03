def foreach(function, numbers):
    for num in numbers:
        yield function(num)


print(list(foreach(lambda x: x * 2, [2, 4, 5])))