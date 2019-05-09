import re
r = re.compile(r'(\w+\.?\w*)\+?\w*?@.+\.com')
print(r.match('tom@hogwarts.com').group(1))
print(r.match('tom.riddle@hogwarts.com').group(1))
print(r.match('tom.riddle+regexone@hogwarts.com').group(1))
print(r.match('tom@hogwarts.eu.com').group(1))
print(r.match('potter@hogwarts.com').group(1))
print(r.match('harry@hogwarts.com').group(1))
print(r.match('hermione+regexone@hogwarts.com').group(1))

