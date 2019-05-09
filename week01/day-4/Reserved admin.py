import re
r = re.compile(r'[Aa]dmin')
print(r.match('Admin'))
print(r.match('admin'))