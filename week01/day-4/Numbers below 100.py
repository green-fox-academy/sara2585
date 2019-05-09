import re
r = re.compile(r"[1-9]?\d?$|100$")
print(r.match('100'))
print(r.match('99'))
print(r.match('0'))
print(r.match('-1'))