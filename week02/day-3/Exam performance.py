import csv
import re
#r1 = re.compile(r"(?P<hour>[\d]+)?h?\:?(?P<minute>[\d]+)?m?\:?(?P<second>[\d]+)?s?")
h = re.compile(r"^([\d]*\.?[\d]+)[h,:]")
m = re.compile(r"([\d]+)m|:([\d]+):")
s = re.compile(r"([\d]+)s|:([\d]+)$")

f = open("exams.tsv", 'r')
tsv_contents  = csv.reader(f)
tsv = []
for line in tsv_contents:
    tsv.append(line[0].split("\t"))
ratios = []
for i in range(1,len(tsv)):
    hours = h.match(tsv[i][2])
    minutes = m.search(tsv[i][2])
    seconds = s.search(tsv[i][2])
    sum = 0.00
    #print(minutes.group(1))
    if hours != None:
      #print(hours.group(1))
      hours = float(hours.group(1))*60
      sum += hours
    if seconds != None:
      if seconds.group(1) != None:
        seconds = float(seconds.group(1))/60
      else:
        seconds = float(seconds.group(2))/60
      sum += seconds
    if minutes != None:
      if minutes.group(1) != None:

        minutes = float(minutes.group(1))
      else:
        minutes = float(minutes.group(2))
      sum += minutes
    if sum != 0:
      ratio = int(tsv[i][1])/sum
    ratios.append(ratio)


        
#print(ratios)
highest_ratio = 0
for i in range(len(ratios)):
  if ratios[i] > highest_ratio:
    highest_ratio = ratios[i]
location = 0
for i in range(len(ratios)):
  if ratios[i] == highest_ratio:
    location = i+1


print(f"The highest points/mins ratio is: {highest_ratio}")
print(f"The highest points/mins ratio located in {tsv[location]}")




