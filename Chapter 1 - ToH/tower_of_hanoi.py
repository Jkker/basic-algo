# Visualization Function Print 3 Poles
def print_poles(*argv):
    p = list(range(0, len(argv)))
    total_rings = 0
    for pole in argv:
        p[pole['label']] = pole['data']
        total_rings += len(pole['data'])
    output = ''
    for arr in p:
        output += str(arr) + ' ' * ((total_rings - len(arr)) * 3 + 2 * (len(arr) != 0))
    print(output)


# Helper Function to Move 1 ring from src to dest
def move_ring(src, dest, print_steps=False):
    ring = src['data'].pop()
    if print_steps: print('moving ring', ring, 'from', src['label'], 'to', dest['label'])
    dest['data'].append(ring)


# Recursive Tower of Hanoi Moving Function
#    Input: Pole src has n smallest rings; pole aux and dest only have larger rings
#    Args: num rings, FROM, TO, AUX
#    Output: Pole dest with n smallest rings in sorted order; all other rings unmoved
def move_tower(n, A, B, C):
    if n > 0:
        move_tower(n - 1, A, C, B)
        move_ring(A, B)
        # print_poles(A, B, C)
        move_tower(n - 1, C, B, A)


def move_tower_green_red(n, A, B, C):
    if n == 0:
        move_ring(A, B)
    else:
        move_tower_green_red(n - 1, A, C, B)
        move_ring(A, B)
        move_tower(n - 1, A, B, C)
        print_poles(A, B, C)
        move_tower_green_red(n - 1, C, B, A)


if __name__ == "__main__":
    a = {'data': [4, 3, 2, 1], 'label': 0}
    b = {'data': [], 'label': 1}
    c = {'data': [], 'label': 2}
    print_poles(a, b, c)
    move_tower(4, a, b, c)
    print_poles(a, b, c)
