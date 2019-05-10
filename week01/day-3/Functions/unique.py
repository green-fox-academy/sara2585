#  Create a function that takes a list of numbers as a parameter

#  Returns a list of numbers where every number in the list occurs only once



def unique(arr):

    n = len(arr)
    
    for i in range(n-2):
        for j in range(i,n-2):
            if arr[i] == arr[j+1]:
                arr.remove(arr[j+1])
                n = n - 1
                i = i - 1

                
                
    return arr



#  Example

print(unique([1, 11, 34, 11, 52, 61, 1, 34]))

#  should print: `[1, 11, 34, 52, 61]`