""" The Making Change Problem
    Input:
        amount - the desired amount of change to be made
        coins - an array of unique coin values
    Output:
        The minimum number of coins needed to add up to amount
"""


# ! Top-down approach
def fewest_coins_recur(amount, coins):
    def recur(val, i):
        if val == 0:
            return 0
        elif i == -1 or val < 0:
            return float('inf')
        else:  # Find the min between the 2 choices
            return min(recur(val - coins[i], i) + 1,  # Include coin i, add 1 to count
                       recur(val, i - 1))  # Not include coin i, proceed to next coin

    return recur(amount, len(coins) - 1)


def fewest_coins_recur_memoized(amount, coins):
    memo = dict()

    def recur(val, i):
        if val == 0:
            return 0
        elif i == -1 or val < 0:
            return float('inf')
        else:  # Find the min between the 2 choices
            if (val, i) in memo.keys():
                return memo[(val, i)]
            else:
                memo[(val, i)] = min(recur(val - coins[i], i) + 1,  # Include coin i, add 1 to count
                                     recur(val, i - 1))  # Not include coin i, proceed to next coin\
                return memo[(val, i)]

    r = recur(amount, len(coins) - 1)
    return r if r != float('inf') else -1


def fewest_coins_queue(amount, coins):
    if amount == 0:
        return 0
    sum_list = [0]
    count_list = [0]
    while sum_list:  # while sum_list is not empty
        curr_sum = sum_list.pop(0)
        curr_count = count_list.pop(0)
        for coin in coins:
            next_sum = curr_sum + coin
            if next_sum == amount:
                return curr_count + 1
            if next_sum < amount:
                sum_list.append(next_sum)
                count_list.append(curr_count + 1)
    return -1


def fewest_coins_queue_memoized(amount, coins):
    # Use a queue for implicit BFS for a tree of possible combinations
    # Return when the first answer at smallest depth is found
    if amount == 0:
        return 0
    # List for memoization
    visited = [False] * amount
    sum_list = [0]
    count_list = [0]
    while sum_list:  # while sum_list is not empty
        curr_sum = sum_list.pop(0)
        curr_count = count_list.pop(0)
        for coin in coins:
            next_sum = curr_sum + coin
            if next_sum == amount:
                print(sum_list)
                return curr_count + 1
            if next_sum < amount and not visited[next_sum]:
                sum_list.append(next_sum)
                count_list.append(curr_count + 1)
                visited[next_sum] = True
    return -1


# ! Bottom-up Approach
def fewest_coins_bfs(amount, coins):  # Has bugs
    count = [float('inf')] * (amount + 1)
    count[0] = 0
    for i, c in enumerate(coins):
        if c <= amount:
            count[c] = 1
            for j in range(1, amount - c + 1):
                if count[j] < count[j + c]:
                    count[j + c] = count[j] + 1
    return count[amount] if count[-1] != float('inf') else -1


def fewest_coins_bfs2(amount, coins):  # Has bugs
    count = [float('inf')] * (amount + 1)
    count[0] = 0
    for j in range(1, amount + 1):
        for c in coins:
            if amount >= c:
                new_count = count[j - c] + 1
                if new_count < count[j]:
                    count[j] = new_count
    return count[amount] if count[-1] != float('inf') else -1


def total_unique_ways(amount, coins):
    sum_list = [0]
    count_list = [0]
    count = 0
    while sum_list:
        curr_sum = sum_list.pop(0)
        curr_count = count_list.pop(0)
        for coin in coins:
            new_sum = curr_sum + coin
            if new_sum < amount:
                sum_list.append(new_sum)
                count_list.append(curr_count + 1)
            if new_sum == amount:
                count += 1
    return count


def fewest_cost_recur(i, CoinVal, Mcost):
    def recur(val, index):
        if val == 0:
            return 0
        elif index == -1 or val < 0:
            return float('inf')
        else:  # Find the min between the 2 choices
            return min(recur(val - CoinVal[index], index) + Mcost[index],  # Include coin i, add 1 to count
                       recur(val, index - 1))  # Not include coin i, proceed to next coin

    return recur(i, len(CoinVal) - 1)


if __name__ == '__main__':
    my_coins = [1, 2, 5]
    # print(total_unique_ways(4, my_coins))
    print(fewest_coins_recur(24, my_coins))
    print(fewest_coins_queue(24, my_coins))
    print(fewest_coins_bfs(24, my_coins))
