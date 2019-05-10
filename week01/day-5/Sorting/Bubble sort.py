def bubble(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = (list[j+1],list[j])
    return list
list1 = [2, 6, 9, 10, 8, 1, 4, 78, 45, 0, 2, 6]
print(bubble(list1))
