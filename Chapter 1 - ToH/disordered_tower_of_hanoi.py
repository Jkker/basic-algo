from tower_of_hanoi import print_poles, move_tower, move_ring


def is_it_there(ring, pole):
    return ring in pole['data']


# Recursive Tower of Hanoi Moving Function
def base_case(n, A, B, C):
    if is_it_there(n, A):
        move_ring(A, B)
    elif is_it_there(n, C):
        move_ring(C, B)


#                         src, dest, aux
def disordered_move_tower(n, A, B, C):
    if n > 0:
        if is_it_there(n, A):
            disordered_move_tower(n - 1, A, C, B)
            move_ring(A, B)
            move_tower(n - 1, C, B, A)

        if is_it_there(n, C):
            disordered_move_tower(n - 1, C, A, B)
            move_ring(C, B)
            move_tower(n - 1, A, B, C)

        if is_it_there(n, B):
            disordered_move_tower(n - 1, A, B, C)


if __name__ == "__main__":
    a = {'data': [3, 2], 'label': 0}
    b = {'data': [4], 'label': 1}
    c = {'data': [5, 1], 'label': 2}
    print_poles(a, b, c)
    disordered_move_tower(5, a, b, c)
    print_poles(a, b, c)
