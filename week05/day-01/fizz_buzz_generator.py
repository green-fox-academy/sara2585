# def fizz_buzz_generator(fizz_buzz):
#     if fizz_buzz% 3 == 0 and fizz_buzz % 5 ==0:
#         yield 'Fizz Buzz'
#     elif fizz_buzz % 3 == 0:
#         yield 'Fizz'
#     elif  fizz_buzz % 5 == 0:
#         yield 'Buzz'
#     else:
#         yield fizz_buzz


def fizz_buzz1(max):
    for i in range(1, max+1):
        if i % 3 == 0 and i % 5 ==0:
            yield 'Fizz Buzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif  i % 5 == 0:
            yield 'Buzz'
        else:
            yield i

fizz_buzz_num = fizz_buzz1(5)
print(next(fizz_buzz_num))
print(next(fizz_buzz_num))


    