import random, timeit


def lomuto_quicksort(L, U, Data):
    if L >= U: return
    pivot = Data[L]
    l = L
    for i in range(L + 1, U + 1):
        if Data[i] < pivot:
            Data[l + 1], Data[i] = Data[i], Data[l + 1]
            l += 1
    Data[L], Data[l] = Data[l], Data[L]
    lomuto_quicksort(L, l - 1, Data)
    lomuto_quicksort(l + 1, U, Data)


def quicksort(L, U, A):
    if L >= U: return
    if A[L] < A[U]:
        A[L], A[U] = A[U], A[L]
    P = A[U]
    B = L
    T = U
    while B < T:
        A[B], A[T] = A[T], A[B]
        B += 1
        T -= 1
        while A[B] < P: B += 1
        while A[T] > P: T -= 1
    A[L], A[T] = A[T], A[L]
    quicksort(L, T - 1, A)
    quicksort(T + 1, U, A)


def test_run(func, max_value, size):
    a = [random.randint(0, max_value) for _ in range(size)]
    start = timeit.default_timer()
    func(0, len(a) - 1, a)
    stop = timeit.default_timer()
    print('{:.4f}'.format(round(stop - start, 4)), end='')


def quicksort_enhanced(L, U, A, k):
    if L + k >= U: return
    if A[L] < A[U]:
        A[L], A[U] = A[U], A[L]
    P = A[U]
    B = L
    T = U
    while B < T:
        A[B], A[T] = A[T], A[B]
        B += 1
        T -= 1
        while A[B] < P: B += 1
        while A[T] > P: T -= 1
    A[L], A[T] = A[T], A[L]
    quicksort_enhanced(L, T - 1, A, k)
    quicksort_enhanced(T + 1, U, A, k)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def test_run2(max_value, size, k):
    a = [random.randint(0, max_value) for _ in range(size)]
    start = timeit.default_timer()
    quicksort_enhanced(0, len(a) - 1, a, k)
    insertion_sort(a)
    stop = timeit.default_timer()
    print('{:.4f}'.format(round(stop - start, 4)), end='')


if __name__ == '__main__':
    for i in range(100):
        test_run2(1, 10000, pow(2, i))
        print('   i =', pow(2, i))
