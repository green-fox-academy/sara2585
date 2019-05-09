import re
r = re.compile(r'-?\d+\,?\d*\.?\d+e?\d+$')
print(r.match('3.14529'))
print(r.match('-255.34'))
print(r.match('128'))
print(r.match('1.9e10'))
print(r.match('123,340.00'))
print(r.match('720p'))

