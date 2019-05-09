import re
r = re.compile(r'\d*?\s?\(?(\d{3})\)?-?\s?\d{3}-?\s?\d{4}')
print(r.match('415-555-1234').group(1))
print(r.match('650-555-2345').group(1))
print(r.match('(416)555-3456').group(1))
print(r.match('202 555 4567').group(1))
print(r.match("4035555678").group(1))
print(r.match('1 416 555 9292').group(1))