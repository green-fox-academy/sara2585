x = [[1,2], [4, 5], [7,8]]
y = [[1,2],[3,4]]
#result = [[0,0], [0,0],[0,0]]
def multiplication(x,y):
    if len(x[0]) != len(y):
        print("x cannot mutiply with y")
    else:
       result = [[0] * len(x[0]) for i in range(len(x))]
       for i in range(len(x)):
            for j in range(len(x[0])):
                for a in range(len(x[0])):             
                    result[i][j] += x[i][a] * y[a][j]
    return result

print(multiplication(x,y))
