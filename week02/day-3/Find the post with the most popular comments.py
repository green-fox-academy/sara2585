import json

#for i in json_contents:
    #if i["comments"] != None:
        #for j in i["comments"]:
           # print(j["like_count"])


def find_most_polular_comments(json_contents):
    #popular = 0
    popular = []
    for i in json_contents:
        if i["comments"] != None:  
            sum = 0          
            for j in i["comments"]:
                sum += j["like_count"]
            popular.append(sum)
    most_like = 0
    for i in popular:
        if i > most_like:
            most_like = i
        

    for i in json_contents:
        if i["comments"] != None:
            sum = 0
            for j in i["comments"]:
                sum += j["like_count"]
        if sum == most_like:
            print(i)



        
                


    #print(popular)
f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-3\\posts.json", 'r')
json_contents = json.load(f)
f.close()
find_most_polular_comments(json_contents)        
        

