import csv

def remove_useless_data(contents):
    for i in contents:
        i = list(str(i).split(","))
     #   print(i)
     
    contents_new = []
    for i in contents:
        if len(i) < 4:
            print(i)
            contents_new.append(i)
        elif i[0] == "" or i[1] == "" or i[3] == "":
            print(i)
            contents_new.append(i)
    for i in contents_new:
        contents.remove(i)
            

f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\election.csv", 'r')
contents = list(csv.reader(f))
remove_useless_data(contents)
f.close()

    