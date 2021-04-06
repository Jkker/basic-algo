def num_of_permutations(n):
    if n == 1:
        return n
    else:
        return n * num_of_permutations(n - 1)


def heapPermutation(a, size, n):
    # if size becomes 1 then prints the obtained permutation
    if size == 1:
        print(a)
        return

    for i in range(size):
        heapPermutation(a, size - 1, n)
        # if size is odd, swap first (0th) and last (size - 1)th element
        # if size is even, swap ith and last (size - 1)th element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


def perm_driver(n):
    def perm_all(height, A):
        if height == 0:
            print(A)
            return
        for i in range(height):
            A[height - 1], A[i] = A[i], A[height - 1]
            perm_all(height - 1, A)
            A[height - 1], A[i] = A[i], A[height - 1]

    buffer = list(range(1, n + 1))
    perm_all(n, buffer)


if __name__ == '__main__':
    print(num_of_permutations(3))
    perm_driver(3)
    # heapPermutation(list(range(1, 3 + 1)), 3, 3)
