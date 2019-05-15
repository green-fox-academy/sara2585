
import csv

def find_oldest_movie(csv_contents):
    contents1 = []
    for i in csv_contents:
        i = list(str(i).split(";"))
        contents1.append(i)

    min = contents1[0]

    for i in contents1:
        if i[1] < min[1]:
            min = i  
    print(min)

f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\movies.csv", "r")
contents = list(csv.reader(f))
find_oldest_movie(contents)
f.close()

