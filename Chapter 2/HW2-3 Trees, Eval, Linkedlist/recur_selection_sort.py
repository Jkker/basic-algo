# Recursive Python3 code to sort 
# an array using selection sort 

# Return minimum index 
def minIndex(a, i, j):
    if i == j:
        return i

        # Find minimum of remaining elements 
    k = minIndex(a, i + 1, j)

    # Return minimum of current  
    # and remaining. 
    return (i if a[i] < a[k] else k)


# Recursive selection sort. n is  
# size of a[] and index is index of  
# starting element. 
def recurSelectionSort(arr, n, index=0):
    # Return when starting and  
    # size are same 
    if index == n:
        print(arr)
        return -1

    # calling minimum index function  
    # for minimum index 
    k = minIndex(arr, index, n - 1)

    # Swapping when index and minimum  
    # index are not same 
    if k != index:
        arr[k], arr[index] = arr[index], arr[k]

    # Recursively calling selection  sort function
    recurSelectionSort(arr, n, index + 1)
    
    if k != index:
        arr[k], arr[index] = arr[index], arr[k]


if __name__ == '__main__':
    # Driver code
    arr = [3, 1, 5, 2, 7, 0]
    n = len(arr)

    # Calling function
    print('Arr:')
    print(arr)
    print('Sorted: ')
    recurSelectionSort(arr, n)
    print('Arr:')
    print(arr)
