#  Create a function that takes a list of numbers as a parameter

#  Returns a list of numbers where every number in the list occurs only once



def unique(arr):

    n = len(arr)
    for i in range(n-2):
        for j in range(i+1,n-1):
            

            if arr[i] == arr[j]:
                arr.remove(arr[j])
                n = n-1
    return arr



#  Example

print(unique([1, 11, 34, 11, 52, 61, 1, 34]))

#  should print: `[1, 11, 34, 52, 61]`