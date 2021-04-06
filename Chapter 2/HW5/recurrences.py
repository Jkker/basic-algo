sum_count = 0


def T1(n):
    global sum_count
    count += 1
    if n <= 1:
        return 1
    else:
        return n * T1(n - 1)


def T2(n):
    global sum_count
    count += 1
    if n <= 1:
        return 1
    else:
        return 2 * T2(n - 1)


def T3(n):
    global sum_count
    count += 1
    if n <= 1:
        return 1
    else:
        return 3 * T3(n - 1) + T3(n - 2)


if __name__ == '__main__':
    print(T3(2))
    print(sum_count)
