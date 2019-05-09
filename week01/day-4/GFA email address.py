import re
r = re.compile(r'^(?P<name>.+\.?.+)@greenfox\.?academy(\.com)?')
print(r.match('john@greenfoxacademy.com').group(1))
print(r.match('jane.doe@greenfoxacademy.com').group(1))
print(r.match('jane@greenfox.academy').group(1))
print(r.match('john@wick.com'))
print(r.match('jane@citromail.hu'))
print(r.match('janegreenfoxacademy.com'))

