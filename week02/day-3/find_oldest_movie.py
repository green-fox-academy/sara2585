
import csv
f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\movies.csv", "r")
contents = list(csv.reader(f))

def find_oldest_movie(contents):
    
    for i in contents:
        i = (str(i).split(";"))

    min = contents[0]
    for i in contents:
        if i[0][1] < min[0][1]:
            min = i  
    print(min)


find_oldest_movie(contents)

