def merging_cost(S):
    def recur(i, j):
        if i == j:
            return S[i]
        else:
            min_cost = float('inf')
            for k in range(i, j):
                merge_cost = recur(i, k) \
                             + max(sum(S[i:k + 1]),
                                   sum(S[k + 1:j + 1])) \
                             + recur(k + 1, j)
                if merge_cost < min_cost:
                    min_cost = merge_cost
            return min_cost

    return recur(0, len(S) - 1)


if __name__ == '__main__':
    sizes = [1, 3, 2]
    print(merging_cost(sizes))
