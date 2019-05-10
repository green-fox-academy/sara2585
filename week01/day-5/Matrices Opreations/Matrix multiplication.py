x = [[1,2],[3,4]]
y = [[1,2], [4, 5], [7,8]]
result = [[0,0], [0,0]]
def multiplication(x,y):
    result = [[0,0], [0,0]]
    for i in range(len(x)):

         for j in range(len(x[0])):
            for a in range(len(y)):
                result[i][j] += x[i][j] * y[a][j]
    return result

print(multiplication(x,y))
