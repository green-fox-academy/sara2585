def insert_sort(list):
    n = len(list)
    for i in range(1,n):
        if list[i-1] > list[i]:
            list[i-1], list[i] = (list[i], list[i-1])
            for j in range(0, i-1):
                if list[j]  > list[i-1]:
                    list[j], list[i-1] = (list[i-1], list[j])
    return list
list1 = [5, 9, 1, 3, 46, 10, 99, 12, 16]
print(insert_sort(list1))



    