import re
r = re.compile(r'^[A-Z]\/\(\s1553\):\s{3}at\swidget\.List\.(\w+)\((ListView\.java):(\d+)\)')
print(r.match('E/( 1553):   at widget.List.makeView(ListView.java:1727)').group(1,2,3))