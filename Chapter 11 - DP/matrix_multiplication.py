def min_scalar_ops_iterative(d):
    look = [[None] * len(d)] * len(d)
    for i in range(0, len(d) - 2):
        look[i][i] = 0

    for offset in range(len(d) - 1):
        for i in range(len(d) - 1 - offset):
            j = offset + i

            look[i][j] = float('inf')
            for k in range(i, j):
                try:
                    b = look[i][k] + look[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                    if look[i][j] > b:
                        look[i][j] = b
                except:
                    print(i, j, k, offset)
    print(look)
    return look


def min_scalar_ops(d):
    def best(i, j):
        if i == j:
            return 0
        else:
            min_ops = float('inf')
            for k in range(i, j):
                num_ops = best(i, k) + d[i] * d[k + 1] * d[j + 1] \
                          + best(k + 1, j)
                if num_ops < min_ops:
                    min_ops = num_ops
            return min_ops

    best_val = best(0, len(d) - 2)
    print(best_val)


def min_scalar_ops_memoized(d):
    memo = [[float('inf')] * (len(d))] * (len(d))  # Lookup Table

    def best(i, j):
        if i == j:
            return 0
        else:
            min_ops = memo[i][j]
            if min_ops != float('inf'):
                return min_ops
            for k in range(i, j):
                num_ops = best(i, k) + d[i] * d[k + 1] * d[j + 1] \
                          + best(k + 1, j)
                if num_ops < min_ops:
                    min_ops = num_ops
            memo[i][j] = min_ops
            return min_ops

    best_val = best(0, len(d) - 2)
    print(best_val)
    print(memo)


def min_scalar_ops_memoized_sp_indices(d):
    memo = [[float('inf')] * len(d)] * len(d)  # Lookup Table
    splitting_indices = [[None] * len(d)] * len(d)

    def best(i, j):
        if i == j:
            return 0
        else:
            min_ops = memo[i][j]
            if min_ops != float('inf'):
                return min_ops
            index = 0
            for k in range(i, j):
                num_ops = best(i, k) + d[i] * d[k + 1] * d[j + 1] \
                          + best(k + 1, j)
                if num_ops < min_ops:
                    min_ops = num_ops
                    index = k
            memo[i][j] = min_ops
            splitting_indices[i][j] = index
            return min_ops

    best_val = best(0, len(d) - 2)
    print(best_val)
    print(splitting_indices)
    print(memo)


if __name__ == '__main__':
    dim = [20, 100, 10, 20, 100, 5]
    min_scalar_ops_iterative(dim)
