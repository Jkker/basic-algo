def diagonal_filling_a(n):
    # Constructing n×n array
    arr = [[0 for i in range(n)] for j in range(n)]
    counter = 1
    for i in range(n):
        arr[i][i] = 0  # the main diagonal
        for j in range(i):
            arr[j][i] = counter  # upper triangle
            counter += 1
    return arr


def diagonal_filling_b(n):
    # Constructing n×n array
    arr = [[0 for i in range(n)] for j in range(n)]
    counter = 1
    for i in range(n):
        arr[i][i] = 0  # the main diagonal
        for j in range(n - i - 1):
            arr[j][j + i + 1] = counter  # upper triangle
            counter += 1
    return arr


def diagonal_filling_c(n):
    # Constructing n×n array
    arr = [[0 for i in range(n)] for j in range(n)]
    counter = 1
    for i in range(n):
        arr[i][i] = 0  # the main diagonal
        for j in range(n - i, n):
            arr[n - i - 1][j] = counter  # upper triangle
            counter += 1
    return arr


if __name__ == '__main__':
    [print(x) for x in diagonal_filling_c(5)]
