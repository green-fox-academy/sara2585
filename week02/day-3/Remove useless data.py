import csv
f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\election.csv", 'r')
contents = list(csv.reader(f))

def remove_useless_data(contents):
    for i in contents:
        i = list(str(i).split(","))

    for i in contents:
        if i[0] == "" or i[1] == "" or i[3] == "":
            print(i)
            contents.remove(i)

 
remove_useless_data(contents)

    