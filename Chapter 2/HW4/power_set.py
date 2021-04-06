def subsets_iter(arr, n):
    # Function to find all subsets of given set.
    # Any repeated subset is considered only
    # once in the output
    _list = []

    # Run counter i from 000..0 to 111..1
    for i in range(2 ** n):
        subset = ""

        # consider each element in the set
        for j in range(n):

            # Check if jth bit in the i is set.
            # If the bit is set, we consider
            # jth element from set
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        # if subset is encountered for the first time
        # If we use set<string>, we can directly insert
        if subset not in _list and len(subset) > 0:
            _list.append(subset)

            # consider every subset
    for subset in _list:

        # split the subset and print its elements
        arr = subset.split('|')
        for string in arr:
            print(string, end=" ")
        print()


subset = []

s = ''


def subsets_recur(A, index=0):
    global subset
    for i in range(index, len(A)):
        subset.append(A[i])
        subsets_recur(A, i + 1)
        subset.pop()
    print(subset)


# Recursive Function
def distinct_subset_recur(S, subset, i):
    if i < 0:  # base case
        print(''.join(subset))
        return
    # normal power set recursion
    subset.append(S[i])
    distinct_subset_recur(S, subset, i - 1)
    subset.pop(0)
    while i > 0 and S[i] == S[i - 1]:  # disregard adjacent duplicates
        i = i - 1
    # recur w/o current element
    distinct_subset_recur(S, subset, i - 1)


# Driver
def driver_distinct_subset_recur(S):
    temp = []
    distinct_subset_recur(S, temp, len(arr) - 1)


if __name__ == '__main__':
    arr = ['a', 'a', 'a', 'b', 'b', 'c']

    s = [['a', 1], ['b', 2], ['c', 3]]
    # print(driver_distinct_subset_recur(arr))
