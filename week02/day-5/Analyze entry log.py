
import csv
import re
r = re.compile(r"(A66 - [\d]{2})")

f = open("logs.csv", "r")
contents = csv.reader(f)


#restore the data as a list:
new_contents = []
for i in contents:
    new_contents.append(i)

#restore the door information because of the messy code
for i in new_contents:
    i[5] = r.match(i[5]).group(1)


floors = ["A66 - 04", "A66 - 12", "A66 - 18"]


groups = []
main = []
second_floor = []
third_floor =[]

#store the log information in groups.
for i in new_contents:
     if i[5] ==floors[0]:
        main.append(i)
     elif i[5] ==floors[1]:         
        second_floor.append(i)
     else:
        third_floor.append(i)

#add name to list:
id_list = set()
for i in new_contents:
    id_list.add(i[12])
#print(id_list)

#restore the name and entry time(list) to a dictionary
entry_check_by_person = {}
for i in id_list:
    entry_time = []    
    for j in new_contents:
        if j[12] == i:
            entry_time.append(j[1])
    entry_check_by_person[i] = entry_time


#print(entry_check_by_person)

#who is the person should we terminate the contract with? (count the late times for each person)
#Who was late the most times?
late_days_by_person= {}
r1 = re.compile(r"^(2019.01.[\d]{2})")     # to catch the date
r2 = re.compile(r"([\d]{1,2}:[\d]{2}:[\d]{2})") # to catch the time 
r3 = re.compile(r"([\d]{1,2}):[\d]{2}:[\d]{2}") # to catch the time and add the hours in group()
r4 = re.compile(r"2019.01.([\d]{2})")
people_who_will_fired =[]
for key in entry_check_by_person:  
    day_list = set()
    for j in entry_check_by_person[key]:
        if int(r4.match(j).group(1)) >= 14:
           day_list.add(r1.match(j).group(1))
#print(len(day_list), key)
    if(len(day_list)) < 11:
        people_who_will_fired.append(key)

#    print(len(day_list), key)
    entry_by_day = {}
    for day in day_list:
        sameday_entry = []
        for a in entry_check_by_person[key]:

            if r1.match(a).group(1) ==day:
                if r2.search(a) != None:
                    sameday_entry.append(r2.search(a).group(1))
        entry_by_day[day] = sameday_entry
    #print(entry_by_day,key)
    late_days = 0
    for day in entry_by_day:
        first_entry_time = entry_by_day[day][0]
        for entry_time in entry_by_day[day]:
            if int(r3.search(entry_time).group(1)) <= int(r3.search(first_entry_time).group(1)):
                first_entry_time = entry_time
        if int(r3.search(first_entry_time).group(1)) >= 9:
            late_days += 1
    late_days_by_person[key] = late_days
#print(late_days_by_person)
most_late_times = 0
for key in late_days_by_person:
    if late_days_by_person[key] > most_late_times:
        most_late_times = late_days_by_person[key]
#print(most_late_times)

#
The_guy_who_late_most_times = ""
for key in late_days_by_person:
    if late_days_by_person[key] == most_late_times:
        The_guy_who_late_most_times = key

#who is the person should we terminate the contract with? (count the late times for each person)



print(f"The guy who late most times is: {The_guy_who_late_most_times}")
print(f"The person should we terminate the contract with are :\n{people_who_will_fired}")

#print(entry_check_by_person["00088:54928"])



# 1 00169:38418
# 1 00075:39296
            

# print(entry_by_day)
    
# print(sameday_entry)


        
 #   print(day_list)


        









            

