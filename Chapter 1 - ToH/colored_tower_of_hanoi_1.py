# Global Variables
counter = 0


def counted_move_ring(A, B):
    global counter
    colored_move_ring(A, B)
    counter += 1


# Visualization Function Print 3 Poles
def colored_print_poles(*argv):
    p = list(range(0, len(argv)))
    total_rings = 0
    for pole in argv:
        p[pole['label']] = pole['data']
        total_rings += len(pole['data'])
    output = ''
    for arr in p:
        c = [str(r['n']) + r['c'] for r in arr]
        output += str(c) + ' ' * ((total_rings - len(arr)) * 6 + 2 * (len(arr) != 0))
    print(output)

    # Helper Function to Move 1 ring from src to dest


def colored_move_ring(src, dest):
    r = src['data'].pop()
    r['c'] = '■' if r['c'] == '□' else '□'
    # print('moving ring', str(r['n']) + r['c'] + 'from pole', src['label'], 'to', dest['label'])
    dest['data'].append(r)


def base_case_1(n, A, B, C):
    if n == 1:  # Base Case
        colored_move_ring(A, B)


def colored_move_tower(n, A, B, C):
    if n == 1:  # Base Case
        counted_move_ring(A, B)
        # print('base case executed')
    elif n >= 2:  # Recursive Case
        colored_move_tower(n - 1, A, C, B)
        counted_move_ring(A, B)
        colored_move_tower(n - 1, C, B, A)


def red_move_tower(n, A, B, C):
    colored_move_tower(n, A, C, B)
    colored_move_tower(n, C, B, A)


def white_move_tower(n, A, B, C):
    if n == 1:
        counted_move_ring(A, B)
    if n >= 2:
        white_move_tower(n - 1, A, B, C)

        counted_move_ring(A, B)
        counted_move_ring(B, C)

        white_move_tower(n - 1, B, A, C)

        counted_move_ring(C, B)

        white_move_tower(n - 1, A, B, C)


def white_move_tower_1(n, A, B, C):
    if n == 1:
        counted_move_ring(A, B)
    else:
        white_move_tower_1(n - 1, A, C, B)

        counted_move_ring(A, B)

        white_move_tower_1(n - 1, C, A, B)
        white_move_tower_1(n - 1, A, B, C)


def white_move_tower_2(n, A, B, C):
    if n == 1:
        counted_move_ring(A, B)
    else:
        colored_move_tower(n - 1, A, C, B)

        counted_move_ring(A, B)

        colored_move_tower(n - 1, C, A, B)
        white_move_tower_2(n - 1, A, B, C)


def white_move_tower_3(n, A, B, C):
    if n == 1:
        counted_move_ring(A, B)
    elif n == 2:
        counted_move_ring(A, C)
        counted_move_ring(A, B)
        counted_move_ring(C, A)
        counted_move_ring(A, B)
    else:
        colored_move_tower(n - 1, A, C, B)
        counted_move_ring(A, B)
        colored_move_tower(n - 2, C, B, A)
        counted_move_ring(C, A)
        colored_move_tower(n - 2, B, C, A)
        counted_move_ring(A, B)
        white_move_tower_2(n - 2, C, B, A)


def colored_create_pole(n, label):
    pole = {'data': [], 'label': label}
    for i in reversed(range(n)):
        pole['data'].append({'n': i + 1, 'c': '■'})
    return pole


if __name__ == "__main__":
    n = 5
    a = colored_create_pole(n, 0)
    b = {'data': [], 'label': 1}
    c = {'data': [], 'label': 2}
    colored_print_poles(a, b, c)
    white_move_tower_2(n, a, b, c)
    colored_print_poles(a, b, c)
    print('\nExecuted', counter, 'times')
