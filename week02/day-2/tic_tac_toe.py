# Write a function that takes a filename as a parameter

# The file contains an ended Tic-Tac-Toe match

# We have provided you some example files (draw.txt, win-x.txt, win-o.txt)

# Return "X", "O" or "Draw" based on the input file



def tic_tac_result(filename):
    try:
        f = open(filename)
        contents = f.readlines()

    except FileNotFoundError:
        print("Cannot find the file")
    except PermissionError:
        print("Cannot read the file")
    
    for i in range(len(contents)):
            if contents[i][0] == contents[i][1] == contents[i][2]:
                if contents[i][0] == "O":
                    return "O"

                else:
                    return "X"

    for j in range(len(contents)):
        if contents[0][j] == contents[1][j] == contents[2][j]:
            if contents[0][j] == "O":
                return "O"
            else:
                return "X"
    
    if contents[0][0] == contents[1][1] == contents[2][2]:
        if contents[0][0] == "O":
            return "O"
        else:
            return "X"

    if contents[0][2] == contents[1][1] == contents[2][0]:
        if contents[0][2] == "O":
            return "O"
        else:
            return "X"
    return "Draw"

print(tic_tac_result("C:\\Users\\Sara_Yu\\Desktop\\Sara\\win-X.txt"))


        


    



#print(tic_tac_result("win-o.txt"))

# Should print "O"



#print(tic_tac_result("win-x.txt"))

# Should print "X"



#
# print(tic_tac_result("draw.txt"))

# Should print "Draw"