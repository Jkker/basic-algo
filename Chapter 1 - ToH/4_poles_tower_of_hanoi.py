from tower_of_hanoi import move_ring, print_poles

# Global Variables
counter = 0


def counted_move_ring(A, B):
    global counter
    move_ring(A, B)
    counter += 1


def base_case_1(n, A, B, C, D):
    if n == 1:
        counted_move_ring(A, B)


def move_tower_4(n, A, B, C, D):
    if n == 1:  # Base Case
        move_ring(A, B)
    elif n >= 2:  # Recursive Case
        move_tower_4(n - 2, A, C, B, D)
        move_ring(A, D)
        move_ring(A, B)
        move_ring(D, B)
        move_tower_4(n - 2, C, B, A, D)


if __name__ == "__main__":
    a = {'data': [5, 4, 3, 2, 1], 'label': 0}
    b = {'data': [], 'label': 1}
    c = {'data': [], 'label': 2}
    d = {'data': [], 'label': 3}
    print_poles(a, b, c, d)
    move_tower_4(5, a, b, c, d)
    print_poles(a, b, c, d)
    print('\nExecuted', counter, 'times')
