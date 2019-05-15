import csv
import re
#r1 = re.compile(r"(?P<hour>[\d]+)?h?\:?(?P<minute>[\d]+)?m?\:?(?P<second>[\d]+)?s?")
h = re.compile(r"^([\d]*\.?[\d]+)[h,:]")
m = re.compile(r"(([\d]+)m|:([\d]+):)")
s = re.compile(r"([\d]+)s|:([\d]+)$")
#r2 = re.compile(r"(\.[\d]+)h")



f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\exams.tsv", 'r')
tsv_contents  = csv.reader(f)
tsv = []
for line in tsv_contents:
    tsv.append(line[0].split("\t"))

for i in range(1,len(tsv)):
    hours = h.match(tsv[i][2])
    minutes = m.search(tsv[i][2])
    seconds = s.search(tsv[i][2])
    sum = 0.00

 #   if hours.group(1):
   #     hours = float(hours.goup(1))*60
   #     sum += hours
   # if seconds:
    #    seconds = float(seconds.group(1))/60
    #    sum += seconds
   # if minutes:
     #   minutes = float(minutes)
     #   sum += minutes

        
    print(sum)




