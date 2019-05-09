import re
r = re.compile(r'^\s+(.+\.+$)')
print(r.match('			The quick brown fox...').group(1))
print(r.match('   jumps over the lazy dog.').group(1))