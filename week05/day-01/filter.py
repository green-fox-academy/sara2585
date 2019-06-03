def filter_sara(func, iterable):
    for item in iterable:
        if func(item):
            yield item

# print(list(filter_sara(lambda x: x > 4, [1, 5, 7])))