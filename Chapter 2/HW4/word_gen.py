subset = []


def word_gen(k, n, servers, index=0):
    global subset
    for i in range(k):
        for j in range(index, servers[i][1]):
            subset.append(servers[i][0])
            word_gen(k, n, servers, i + 1)
            subset.pop()
    print(''.join(subset))


def subsets_recur(A, index=0):
    global subset
    for i in range(index, len(A)):
        subset.append(A[i])
        subsets_recur(A, index + 1)
        subset.pop()
    print(subset)


def word_gen_rec(k, n, servers, word=''):
    if n == 0:
        print(word)
        return
    for i in range(k):
        for j in range(servers[i][1]):
            new_word = word + servers[i][0]
            word_gen_rec(k, n - 1, servers, new_word)


def missi_driver(n):
    global server
    buffer = list(range(1, n + 1))
    missi(n, len(server), buffer, server)


def missi(depth, k, buffer, server):
    if depth == 0:
        print(buffer)
        return
    else:
        for i in range(k):
            [letter, num_of_letter_left] = server[i]
            buffer[depth] = letter
            num_of_letter_left -= 1
            server[i] = [letter, num_of_letter_left]
            if num_of_letter_left == 0:
                buffer[depth - 1], buffer[i] = buffer[i], buffer[depth - 1]
                missi(depth - 1, k, buffer, server)
                buffer[depth - 1], buffer[i] = buffer[i], buffer[depth - 1]
            else:
                missi(depth - 1, k, buffer, server)


if __name__ == '__main__':
    s = [['a', 1], ['b', 2], ['c', 3]]
    word_gen(len(s), 6, s)
