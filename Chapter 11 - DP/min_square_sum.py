def min_square_sum(A):
    def recur(i, j):
        if i == j:
            return 0
        elif i == j - 1:
            return pow(A[i], 2)
        else:
            min_sum = float('inf')
            for k in range(i, j):
                curr_sum = squared_sum(i, k) + squared_sum(k + 1, j) + recur(i, k) + recur(k + 1, j)
                if curr_sum < min_sum:
                    min_sum = curr_sum
            return min_sum

    def squared_sum(i, j):
        s = pow(sum(A[i:j]), 2)
        return s

    return recur(0, len(A))


def min_square_sum2(A):
    lookup = [None] * (len(A) + 1)

    def recur(i):
        if i == len(A) + 1:
            return 0
        elif lookup[i] is not None:
            return lookup[i]
        else:
            min_sum = float('inf')
            for k in range(i, len(A) + 1):
                curr_sum = pow(sum(A[i:k + 1]), 2) + recur(k + 1)
                if curr_sum < min_sum:
                    min_sum = curr_sum
            lookup[i] = min_sum
            return min_sum

    return recur(1)


if __name__ == '__main__':
    arr = [0, 6, 1, -7, 5, 8]
    # arr = [None, 1, 2, 3]
    print(min_square_sum2(arr))
