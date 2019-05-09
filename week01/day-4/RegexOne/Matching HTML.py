import re
r = re.compile(r'\<(\w+).*\>.+\<\/\1\>')
print(r.match('<a>This is a link</a>').group(1))
print(r.match("<a href='https://regexone.com'>Link</a>").group(1))
print(r.match("<div class='test_style'>Test</div>").group(1))
print(r.match("<div>Hello <span>world</span></div>").group(1))