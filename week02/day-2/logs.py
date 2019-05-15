# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.
import re
r = re.compile(r"[\d]{2}\.[\d]{2,3}\.[\d]{2}\.[\d]{2}")


f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\log.txt", "r")
contents = f.read()
#print(contents)

def catch_IP(contents):
    r = re.compile(r"[\d]{2}\.[\d]{2,3}\.[\d]{2}\.[\d]{2}")
  #  f = open("C:\\Users\\Sara_Yu\\Desktop\\Sara\\log.txt", "r")
    contents = f.read()
    return r.findall(contents)



print(catch_IP(contents))

def catch_request(contents):
    r = re.compile(r"POST")
    p = len(r.findall(contents))
    g =len(re.compile(r"GET").findall(contents))
    return f"the ratio for GET is {g/(g+p)}, the ratio for POST is {p/(g+p)}"
    

print(catch_request(contents))
    




