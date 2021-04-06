import numpy as np


def greatest_common_subsequence(s1, s2):
    """
    :param s1: String 1
    :param s2: String 2
    :return: Length of the Greatest Common Subsequence
    """

    def len_recur(i, j):
        if i < 0 or j < 0:
            return 0
        if s1[i] == s2[j]:
            length = 1 + len_recur(i - 1, j - 1)
        else:
            length = max(len_recur(i, j - 1),
                         len_recur(i - 1, j))
        return length

    return len_recur(len(s1) - 1, len(s2) - 1)


def greatest_common_subsequence_memoized(s1, s2):
    """
    :param s1: String 1
    :param s2: String 2
    :return: Length of the Greatest Common Subsequence
    """

    lookup = [[-1] * len(s1)] * len(s2)  # Initialize cells in the lookup table to -1

    def len_recur(i, j):
        if i < 0 or j < 0:
            return 0
        length = lookup[i][j]
        if length != -1:
            return length
        elif s1[i] == s2[j]:
            length = 1 + len_recur(i - 1, j - 1)
        else:
            length = max(len_recur(i, j - 1),
                         len_recur(i - 1, j))
        lookup[i][j] = length
        return length

    return len_recur(len(s1) - 1, len(s2) - 1)


def greatest_mismatching_subsequence_memoized(s1, s2):
    """
    :param s1: String 1
    :param s2: String 2
    :return: Length of the Greatest Mismatching Subsequence
    """

    lookup = [[-1] * len(s1)] * len(s2)  # Initialize cells in the lookup table to -1

    def len_recur(i, j):
        if i < 0 or j < 0:
            return 0
        length = lookup[i][j]
        if length != -1:
            return length
        elif s1[i] != s2[j]:
            length = 1 + len_recur(i - 1, j - 1)
        else:
            length = max(len_recur(i, j - 1),
                         len_recur(i - 1, j))
        lookup[i][j] = length
        return length

    return len_recur(len(s1) - 1, len(s2) - 1)


L = []


def greatest_common_subsequence_path_memoized(s1, s2):
    lookup = [[-1] * (len(s2) + 1)] * (len(s1) + 1)  # Initialize cells in the lookup table to -1
    whereto = [[None] * (len(s2) + 1)] * (len(s1) + 1)

    def len_recur(i, j):
        if i < 0 or j < 0:
            return 0
        length = lookup[i][j]
        if length != -1:
            return length
        elif s1[i] == s2[j]:
            length = 1 + len_recur(i - 1, j - 1)
            r, s = i - 1, j - 1
        else:
            length = max(len_recur(i, j - 1),
                         len_recur(i - 1, j))
            if length == len_recur(i, j - 1):
                r, s = i, j - 1
            else:
                r, s = i - 1, j
        lookup[i][j] = length
        whereto[i][j] = [r, s]
        return length

    def print_path(i, j):
        if i > 0 and j > 0:
            [r, s] = whereto[i][j]
            print_path(r, s)
            if r == i - 1 and s == j - 1:
                print(s1[i], end='')

    try:
        return len_recur(len(s1) - 1, len(s2) - 1)
    finally:
        global L
        L = lookup
        # print(lookup)
        # print_path(len(s1) - 1, len(s2) - 1)
        # print()


def build_string(A, B, Look):
    def recur(i, j):
        if i == 0 or j == 0: return ''
        if A[i] == B[j]:
            print(A[i])
            return recur(i, j) + A[i]
        elif i != 0 and Look[i][j] == Look[i - 1][j]:
            return recur(i - 1, j)
        else:
            return recur(i, j - 1)

    return recur(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    A = 'bcaax'
    B = 'bcda'
    print(greatest_common_subsequence_path_memoized(A, B))
    print(L)
    print(build_string(A, B, L))
