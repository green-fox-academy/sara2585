def map_sara(function, iterable):
    for item in iterable:
        yield function(item)


