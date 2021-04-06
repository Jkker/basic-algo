from collections import deque


class Node:
    def __init__(self, data, *children):
        self.val = data  # Assign data
        self.children = list(children)
        self.small = None
        self.which = None
        self.numb = None
        self.dis = None
        self.dis1 = None
        self.dis2 = None

    def __repr__(self):
        return str(self.val)


# ? Tree Traversals Functions
def preorder(root):
    if root:
        print(root.val, end=' ')
        for child in root.children:
            preorder(child)


def postorder(root):
    if root:
        for child in root.children:
            postorder(child)
        print(root.val, end=' ')


def postorder_reverse(root):
    if root:
        for child in reversed(root.children):
            postorder(child)
        print(root.val, end=' ')


def preorder_reverse(root):
    if root:
        print(root.val, end=' ')
        for child in reversed(root.children):
            preorder_reverse(child)


def breadth_first_traversal(root):
    nodes = deque([root])
    while len(nodes):
        node = nodes.popleft()
        print(node.val, end=' ')
        for child in node.children:
            nodes.append(child)


def postorder_fields(root, field):
    if root:
        for child in root.children:
            postorder_fields(child, field)
        print(getattr(root, field), end=' ')


def preorder_fields(root, field):
    if root:
        print(getattr(root, field), end=' ')
        for child in root.children:
            preorder_fields(child, field)


# ? HW Answers
def store_smallest(root):
    if root is None:
        return
    else:
        root.small = root.val
        for child in root.children:
            store_smallest(child)
            if child.small < root.small:
                root.small = child.small


def store_smallest_which(root):
    if root is None:
        return
    else:
        root.small = root.val
        root.where = root
        for child in root.children:
            store_smallest_which(child)
            if child.small < root.small:
                root.small = child.small
                root.where = child


def store_leaf_number(root):
    if root is None:
        return
    elif not root.children:  # Root is a leaf
        root.numb = 1
    else:  # Root is a inner vertex
        numb = 0
        for child in root.children:
            store_leaf_number(child)
            numb += child.numb
        root.numb = numb


def store_distance(root):
    if root is None:
        return
    elif not root.children:  # Root is a leaf
        root.dis = 0
    else:  # Root is a inner vertex
        dis = 0
        for child in root.children:
            store_distance(child)
            if child.dis >= dis:
                dis = child.dis + 1
        root.dis = dis


def store_distance_2(root):
    if root is None:
        return
    elif not root.children:  # Root is a leaf
        root.dis1 = 0
        root.dis2 = float('-inf')  # Set leaf.dis2 to —∞.
    else:  # Root is a inner vertex
        dis_array = [float('-inf')]  # Set default value for
        # vertices with one children
        for child in root.children:
            store_distance_2(child)
            dis_array.append(child.dis1 + 1)
        dis_array.sort()
        root.dis1 = dis_array[-1]
        root.dis2 = dis_array[-2]


def preorder_parent(root, parent):
    if root:  # Root is not None
        if parent:  # Parent is not None
            print((root.val, parent.val), end=' ')
        else:
            print((root.val, None), end=' ')
        for child in root.children:
            preorder_parent(child, root)


def postorder_parent(root, parent):
    if root:  # Root is not None
        for child in root.children:
            postorder_parent(child, root)
        if parent:  # Parent is not None
            print((root.val, parent.val), end=' ')
        else:
            print((root.val, None), end=' ')


def preorder_parent2(root):
    if root:  # Root is not None
        for child in root.children:
            print((child.val, root.val), end=' ')
            preorder_parent2(child)


def postorder_parent2(root):
    if root:  # Root is not None
        for child in root.children:
            postorder_parent2(child)
            print((child.val, root.val), end=' ')


backpack = 0


def rotate(root):
    global backpack
    if root:
        for child in root.children:
            rotate(child)
        # Swap .val with what's in the backpack
        root.val, backpack = backpack, root.val


if __name__ == '__main__':
    Tr = Node(2,
              Node(9,
                   Node(0)),
              Node(8),
              Node(6,
                   Node(1,
                        Node(3),
                        Node(4),
                        Node(5,
                             Node(2))),
                   Node(7)))
    T = Node('A',
             Node('B',
                  Node('F'),
                  Node('G')),
             Node('C'),
             Node('D'),
             Node('E'))
    S = Node('A',
             Node('B',
                  Node('F',
                       Node('G')),
                  Node('C',
                       Node('D',
                            Node('E')))))

    X = Node(1,
             Node(2),
             Node(3,
                  Node(5),
                  Node(6)),
             Node(4))
    N = Node(0,
             Node(1),
             Node(2,
                  Node(4,
                       Node(6),
                       Node(7))),
             Node(3,
                  Node(5)))
    # postorder_parent2(T)
    store_smallest(Tr)
    # store_distance(Tr)
    store_smallest_which(Tr)
    postorder(Tr)
    print()
    postorder_fields(Tr, 'small')
    print()

    from pptree import print_tree

    print_tree(Tr, horizontal=False)
    print_tree(Tr, "children", "small", horizontal=False)
    # postorder_fields(Tr, 'where')
    # print('T:')
    # postorder_parent(T, None)
    # print('\nS:')
    # postorder(S)
