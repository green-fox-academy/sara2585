x = [[6,3,2],[7,2,4], [3,4,1]]
y = [[3,7,3], [1,9,2], [2,12,4]]

def subtrction(x,y):
    result = [[0] * len(x[0]) for i in range(len(x))]
    n = len(x)
    l = len(x[0])

    for i in range(n):
         for j in range(l):
             result[i][j] = x[i][j] - y[i][j]
    return result
print(subtrction(x,y))
