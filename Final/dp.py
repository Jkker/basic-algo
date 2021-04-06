def matrix_multiplication_memoized(D):
    memo = [[0 for _ in range(len(D) - 1)] for _ in range(len(D) - 1)]

    def cost(i, j):
        if i == j:
            return 0
        elif memo[i][j]:
            return memo[i][j]
        else:
            min_cost = float('inf')
            for k in range(i, j):
                curr_cost = cost(i, k) + cost(k + 1, j) + \
                            D[i] * D[k + 1] * D[j + 1]
                if min_cost > curr_cost:
                    min_cost = curr_cost
            memo[i][j] = min_cost
            return min_cost

    best = cost(0, len(D) - 2)
    print(best)
    print(memo)
    return best


def matrix_multiplication_store_decisions(D):
    memo = [[0 for _ in range(len(D))] for _ in range(len(D))]
    decisions = [[0 for _ in range(len(D))] for _ in range(len(D))]

    def cost(i, j):
        if i == j:
            return 0
        elif memo[i][j]:
            return memo[i][j]
        else:
            min_cost = float('inf')
            best_k = None
            for k in range(i, j):
                curr_cost = cost(i, k) + cost(k + 1, j) + D[i] * D[k + 1] * D[j + 1]
                if min_cost > curr_cost:
                    min_cost = curr_cost
                    best_k = k
            memo[i][j] = min_cost
            decisions[i][j] = best_k
            return min_cost

    best = cost(0, len(D) - 2)
    # print(best)
    # print(memo)
    # print(decisions)
    return best, decisions


from binary_tree import Node, inorder, inorder_fields


# from binarytree import Node


def build_tree(decisions):
    def recur(i, j):
        if i == j:
            return Node('M' + str(i + 1))
        k = decisions[i][j]
        node = Node()
        node.left = recur(i, k)
        node.right = recur(k + 1, j)
        node.val = node.right.val + ' x ' + node.left.val
        return node

    return recur(0, len(decisions) - 2)


# def longest_increasing_subsequence(A):
#     def recur(i, j):
#         if i == j:
#             return 1
#         elif i == j - 1:
#             if A[j] > A[i]:
#                 return 2
#         else:
#             if A[j] > A[i]:
#                 return recur(i, j + 1) + 1
#             else:
#                 return recur(i + 1, j)
# 
#     return recur(0, len(A))
def longest_increasing_subsequence(nums):
    memo = [1] * len(nums)
    max_len = 1
    for i in range(1, len(nums)):

        for j in range(0, i):
            if nums[i] > nums[j]:
                if memo[i] < memo[j] + 1:
                    memo[i] = memo[j] + 1

        if max_len <= memo[i]:
            max_len = memo[i]

    return max_len


if __name__ == '__main__':
    # dim = [20, 100, 10, 20, 100, 5]
    # dim = [30, 35, 15, 5, 10, 20, 25]
    # best_cost, decisions = matrix_multiplication_store_decisions(dim)
    # print(f'Best Cost: {best_cost}')
    # t = build_tree(decisions)
    # print(t)
    print(longest_increasing_subsequence([6, 2, 1, 3, 5, 4, 7, 2, 8, 2, 2, 2]))
