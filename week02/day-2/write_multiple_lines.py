
# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.

def write_multiple_lines(path, word, num):
    try:
        f = open(path, "w")
        for i in range(num):
           f.writelines(word + "\n")
        f.close()
    except PermissionError:
        print("Cannot write the file")


write_multiple_lines("C:\\Users\\Sara_Yu\\Desktop\\Sara\\greenfox\\sara_repo\\week02\\day-2\\my-file.txt", "Sara", 3)
