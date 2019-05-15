
# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(copyfromfile,copytofile):
    try:
        f1 = open(copyfromfile, "r")
        f2 = open(copytofile, "w")
        contents = f1.readlines()
        for content in contents:
            f2.writelines(content + "\n")
        f1.close()
        f2.close()
        return True
    except FileNotFoundError:
        return False
    except PermissionError:
        return False

print(copy_file("sara test.txt", "write.txt"))
    

        