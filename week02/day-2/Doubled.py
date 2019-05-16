f =open("duplicated-chars.txt", 'r')
contents = f.readlines()
contents_list = []
for i in contents:
    i = i.split("  ")
    contents_list.append(i)
for i in contents_list:
    print(i)

new_contents = []
for i in contents_list:
    for j in i:
        new_contents.append(j[::2])

final_contents= []

final_contents.append(" ".join(new_contents))

print(final_contents)



    