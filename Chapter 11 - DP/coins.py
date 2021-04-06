def num_combo_sum_to(coins, T):
    count = [[0] * T] * len(coins)
    print(count)
    count[0][0] = 1
    for j in range(T):
        for i, c in enumerate(coins):
            if i < 0 or j < 0:
                count[i][j] = 0
            count[i][j] = count[i - 1][j] + \
                          count[i][j - c]
    print(count)
    return count[len(coins) - 1][T - 1]


def find_count(coins, T):
    count_arr = {0: 1}
    for i in count_arr:
        for j, coin in enumerate(coins):
            print('i: ', i, 'coin: ', coin)
            if i + coin not in count_arr:
                count_arr[i + coin] = 0
            count_arr[i + coin] += count_arr[i]
    return count_arr[T - 1]


def find_count1(coins, T):
    count_arr = [float('inf')] * (T + 1)
    for i, c in enumerate(coins):
        count_arr[c] = 1
        for j in range(1, T - c):
            if count_arr[i] + 1 < count_arr[i + c]:
                count_arr[i + c] = count_arr[i] + 1
    return count_arr[T]


if __name__ == '__main__':
    Coins = [1, 2, 3]
    # num_combo_sum_to(6, 2)
    print(num_combo_sum_to(Coins, 6))
