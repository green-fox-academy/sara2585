
# Write a function that is able to manipulate a file
# By writing your name into it as a single line
# The file should be named "my-file.txt"
# In case the program is unable to write the file,
# It should print the following error message: "Unable to write file: my-file.txt"

def write_single_line(name):
    try:
        f = open("my-file.txt", "w")
        f.write(name)
        f.close()
    except PermissionError:
        print("Unable to write file: my-file.txt")

write_single_line("Sara")