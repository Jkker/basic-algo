from arbitrary_tree import preorder


class Node:
    def __init__(self, val, *children):
        self.val = val
        self.children = list(children)
        self.dis = 0
        self.color = None
        self.bool = True


def color_win_loss(root):
    if not root.children:  # root is a Leaf
        root.color = 'green'
    else:  # root is a inner vertex
        min_dis_child = root.children[0]
        for child in root.children:
            color_win_loss(child)
            # Find distance to the furthest leaf
            if root.dis <= child.dis:
                root.dis = child.dis + 1
            # Find the min distance in all children
            if min_dis_child.dis > child.dis:
                min_dis_child = child
        # Set color to the opposite of that of the min distance child
        if min_dis_child.color == 'red':
            root.color = 'green'
        else:
            root.color = 'red'
    print(root.val, root.color)


def bool_win_loss(root):
    root.bool = True  # initialize to True
    if root.children:  # processing inner vertices
        for child in root.children:
            bool_win_loss(child)
            root.bool = root.bool and not child.bool
    print(root.val, root.bool, end=' ')


def a_to_move(root):
    root.bool = True  # initialize to True
    if root.children:  # processing inner vertices
        root.bool = root.children[0].bool
        for child in root.children:
            b_to_move(child)
            root.bool = root.bool or child.bool
    print(root.val, root.bool, end=' ')


def b_to_move(root):
    root.bool = True  # initialize to True
    if root.children:  # processing inner vertices
        root.bool = root.children[0].bool
        for child in root.children:
            a_to_move(child)
            root.bool = root.bool and child.bool
    print(root.val, root.bool, end=' ')


def store_sum_to_leaves(root):
    for child in root.children:
        child.val += root.val  # preorder sum calculation
        store_sum_to_leaves(child)
    if root.children:  # postorder clean up inner vertices
        root.val = 0


if __name__ == '__main__':  # main function
    T = Node(0,
             Node(1,
                  Node(1.2)),
             Node(2),
             Node(3,
                  Node(5,
                       Node(7,
                            Node(8)),
                       Node(6))),
             Node(4,
                  Node(9),
                  Node(10),
                  Node(11,
                       Node(12))))

    T1 = Node(1, Node(1, Node(1)))

    # Call to initiate the process
    # bool_win_loss(T)
    # print()
    # a_to_move(T)
    store_sum_to_leaves(T)
    preorder(T)
