from tower_of_hanoi import move_ring, print_poles

# Global Variables
counter = 0


def counted_move_ring(A, B):
    global counter
    move_ring(A, B)
    counter += 1


# The bunny-hop solution
# Slower than the co-recursive solution
def circular_move_tower_hop(n, A, B, C):
    if n == 1:  # Base Case
        counted_move_ring(A, B)
    elif n >= 2:  # Recursive Case
        circular_move_tower_hop(n - 1, A, B, C)
        circular_move_tower_hop(n - 1, B, C, A)
        counted_move_ring(A, B)
        circular_move_tower_hop(n - 1, C, A, B)
        circular_move_tower_hop(n - 1, A, B, C)


# The first recursive function to move the tower by 1 step
def circular_move_tower(n, A, B, C):
    if n == 1:  # Base Case
        counted_move_ring(A, B)
    elif n >= 2:  # Recursive Case
        circular_move_tower_2(n - 1, A, B, C)
        counted_move_ring(A, B)
        circular_move_tower_2(n - 1, C, A, B)


# The second recursive function to move the tower by 2 steps
def circular_move_tower_2(n, A, B, C):
    if n == 1:  # Base Case
        counted_move_ring(A, B)
        counted_move_ring(B, C)
    if n >= 2:
        circular_move_tower_2(n - 1, A, B, C)
        counted_move_ring(A, B)
        circular_move_tower(n - 1, C, A, B)
        counted_move_ring(B, C)
        circular_move_tower_2(n - 1, A, B, C)
        # circular_move_tower(n - 1, A, B, C)
        # circular_move_tower(n - 1, B, C, A)


def create_pole(n, label):
    pole = {'data': [], 'label': label}
    for i in reversed(range(n)):
        pole['data'].append(i + 1)
    return pole


if __name__ == "__main__":
    n = 3
    a = create_pole(n, 0)
    b = {'data': [], 'label': 1}
    c = {'data': [], 'label': 2}
    print_poles(a, b, c)
    # circular_move_tower(n, a, b, c)
    circular_move_tower_hop(n, a, b, c)
    print_poles(a, b, c)
    print('\nExecuted', counter, 'moves')
