#Matching phone numbers in China
import re
r = re.compile(r'1[3456789]\d{9}$')
print(r.match('15005272485'))
print(r.match('150052724852'))