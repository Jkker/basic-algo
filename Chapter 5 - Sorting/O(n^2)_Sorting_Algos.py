def bubble_sort(A):
    for iteration in range(len(A)):
        for i in range(iteration):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


if __name__ == '__main__':
    a = [3, 1, 2, 4]
    insertion_sort(a)
    # bubble_sort(a)
    print(a)
