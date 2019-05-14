# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"
try:
    f = open("..\..\day-2\\my-file.txt", "r")
    contents = f.readlines()
    for line in contents:
        print(line)
    f.close()
except FileNotFoundError:
    print("Unable to read file: my-file.txt")