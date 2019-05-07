
current_hours = 14

current_minutes = 34

current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a

# day if the current time is represented by the variables

hours = 24 - current_hours
minutes = 60 -34
seconds = 60-42
remaining_minutes = seconds + (minutes - 1)*60 + (hours - 1)*60*60
print("The remaining seconds is: {}".format(remaining_minutes))