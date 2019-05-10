x = [[3,2,3], [11,1,6], [3, 4, 4]]
def main_anti_dia_mirror(x):
    result = [[0] * len(x[0]) for i in range(len(x))]
    n = len(x)
    m = len(x[0])
    for i in range(n):
        for j in range(m):
            result[i][j] = x[n-1-i][m-1-j]
    return result
print(main_anti_dia_mirror(x))