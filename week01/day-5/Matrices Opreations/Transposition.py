x = [[3,2,3], [11,1,6], [3, 4, 4]]
def trans(x):
    result = [[0] * len(x[0]) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[j][i]
    return result
print(trans(x))