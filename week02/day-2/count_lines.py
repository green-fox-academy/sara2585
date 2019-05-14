# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines(file_name):
    try:
       f = open(file_name, "r")
       contents = f.readlines()
       count = 0
       count = len(contents)
       return count
    except FileNotFoundError:
        return 0
    
file = count_lines("my-file.txt")
print(file)
