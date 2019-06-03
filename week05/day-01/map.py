def map(function, iteable):
    for item in iteable:
        yield function(item)


