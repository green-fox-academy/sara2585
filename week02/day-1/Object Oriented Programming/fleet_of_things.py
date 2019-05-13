from fleet import Fleet

from thing import Thing

fleet = Fleet()

# Create a fleet of things to have this output:

list = ["Get milk", "Remove the obstacles", "Stand up", "Eat lunch"]
things = []

for i in list:
    
    if i == "Stand up" or i == "Eat lunch":

        Thing(i).complete()
        things.append(Thing(i))
    else:
        things.append(Thing(i))

for i in things:
    fleet.add(i)
    if i.name == "Stand up" or i.name == "Eat lunch":
        i.complete()
    
print(f'{fleet.__str__}')
        

    
        
fleet
# 1. [ ] Get milk

# 2. [ ] Remove the obstacles

# 3. [x] Stand up

# 4. [x] Eat lunch



print(fleet)