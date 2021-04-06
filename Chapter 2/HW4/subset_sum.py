sum_count = 0


def subset_sum(A, target, depth=0):
    global sum_count
    if depth == len(A) and target == 0:
        sum_count += 1
    elif depth < len(A):
        subset_sum(A, target, depth + 1)  # not include letter A[i]
        subset_sum(A, target - A[depth], depth + 1)  # include letter A[i]
    return


def subset_sum_size(A, target, depth=0, size=0):
    global sum_count
    if size > len(A) / 2 or target < 0:
        return
    if target == 0 and size == len(A) / 2:
        sum_count += 1
    elif depth < len(A):
        subset_sum_size(A, target, depth + 1, size)  # not include letter A[i]
        subset_sum_size(A, target - A[depth], depth + 1, size + 1)  # include letter A[i]
    return


if __name__ == '__main__':
    Coins = [1, 2, 3, 4]
    # subset_sum(Coins, 7)
    subset_sum_size(Coins, 7)
    print('count:', sum_count)
# print(find_coins_sum(Coins, 9))
