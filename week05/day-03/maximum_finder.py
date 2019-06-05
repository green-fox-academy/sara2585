def maximum_finder(arr, maximum = None):
    if len(arr) == 1:
        if maximum is None:
            maximum = arr[0]
            return maximum
        elif maximum > arr[0]:
            return maximum
        else:
            return arr[0]
    if maximum is None or maximum < arr[0]:
        maximum = arr[0]
        return maximum_finder(arr[1:], maximum)
    else:
        return maximum_finder(arr[1:], maximum)

print(maximum_finder([5, 2, 6, 7, 10,20, 0]))

print(maximum_finder([5]))
print(maximum_finder([5, 2, 6]))
print(maximum_finder([5, 2, 6, 7, 1]))