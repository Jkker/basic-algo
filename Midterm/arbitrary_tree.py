from collections import deques


class Node:
    def __init__(self, data, *children):
        self.dat = data  # Assign data
        self.children = list(children)
        self.gold = 0
        self.count = None


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


def inorder(root):
    c = root.children
    if len(c) > 2: raise Exception('Node ' + str(root.val) + ' has more than 2 children')
    if len(c) > 0: inorder(root.children[0])
    print(root.val, end=' ')
    if len(c) > 1: inorder(root.children[1])


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


Child = []


def store_sum_gold(v):
    global Child
    if v is None:
        return
    elif not Child[v]:  # v is a leaf
        v.count = v.gold
    else:  # v is a inner vertex
        v.count = 0
        for c in Child[v]:
            store_sum_gold(c)
            v.count += c.count


def store_distance_gold(v):
    global Child
    if v is None:
        return
    elif not Child[v]:  # v is a leaf
        v.count = 0 if v.gold == 1 else float('inf')
    else:  # v is a inner vertex
        v.count = 0 if v.gold == 1 else float('inf')
        for c in Child[v]:
            store_distance_gold(v)
            if c.count <= v.count:
                v.count = c.count + 1


def find_nearest_gold(v):
    q = Queue([v])
    while len(q):  # queue is not empty
        w = q.popleft()
        if w.gold == 1: return w
        print(w.val, end=' ')
        for child in w.children:
            q.append(child)


if __name__ == '__main__':
    T = Node('A',
             Node('B'),
             Node('C',
                  Node('E'),
                  Node('F'),
                  ),
             Node('D')
             )
    preorder(T)
    print()
    postorder(T)
