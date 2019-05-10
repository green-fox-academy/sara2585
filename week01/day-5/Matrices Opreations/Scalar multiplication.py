x = [[6,3,2],[7,2,4], [3,4,1]]

def scalar_multiplication(n,x):
    
    result = [[0] * len(x[0]) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = n * x[i][j]

    return result
print(scalar_multiplication(4,x))

