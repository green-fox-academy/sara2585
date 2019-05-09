import re
r = re.compile(r'^<img\s.*src="(.*)">')
m = r.match('<img src="dog.png">')
print(m.group(1))

m1 = r.match('<img alt="Cat picture" src="./images/cat-01.png">')
print(m1.group(1))

m1 = r.match('<script src="jquery.js"></script>')
print(m1)