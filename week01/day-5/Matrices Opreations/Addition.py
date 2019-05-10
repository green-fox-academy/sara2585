def add(x, y):
    n1 = len(x)
    n2 = len(x[0])
    #result = [[0,0,0], [0,0,0], [0,0,0]]
    result = [[0] * len(x[0]) for i in range(len(x))]

    for i in range(n1):

        for j in range(n2):
            result[i][j] = x[i][j] + y[i][j]
    return result

x = [[2,5,7], [1,4,2], [6,2,8]]
y = [[3,2,3], [11,1,6], [3, 4, 4]]

print(add(x,y))