from collections import deque
from pptree import print_tree


class Node:
    def __init__(self, data, *children):
        self.val = data  # Assign data
        self.children = list(children)
        self.count = None
        self.dist = None
        self.gold = 0
        self.pred = None
        self.succ = None
        self.Allsame = None

    def __str__(self):
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
    while nodes:
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


def store_edge_count(root):
    def _recur(vertex):
        if vertex:
            for child in vertex.children:
                child.count = vertex.count + 1
                _recur(child)

    if root:
        root.count = 0
        _recur(root)


def store_dist_to_deepest_leaf(root):
    if root:
        root.dist = 0
        for child in root.children:
            store_dist_to_deepest_leaf(child)
            if root.dist <= child.dist:
                root.dist = child.dist + 1


def store_leaf_numb(root):
    if root:
        root.count = 1
        for child in root.children:
            store_leaf_numb(child)
            if root.count <= child.count:
                root.count += child.count


def store_gold_dist(root):
    if root:
        root.dist = 0 if root.gold else float('inf')
        for child in root.children:
            store_gold_dist(child)
            if root.dist >= child.dist:
                root.dist = child.dist + 1


def store_gold_dist_on_root_path(root):
    root.dist = 0 if root.gold else float('inf')

    def _recur(root):
        if root:
            for child in root.children:
                child.dist = 0 if child.gold else float('inf')
                if root.dist <= child.dist and not child.gold:
                    child.dist = root.dist + 1
                _recur(child)

    return _recur(root)


def store_gold_dist_on_root_path_bfs(root):
    root.dist = 0 if root.gold else float('inf')
    queue = [root]
    while queue:
        v = queue.pop(0)
        for c in v.children:
            if c.gold:
                c.dist = 0
            else:
                c.dist = v.dist + 1
            queue.append(c)


def bfs(root, value):
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val == value:
            return node
        for child in node.children:
            q.append(child)


temp = None


def store_pred(root):
    global temp
    if root:
        for child in root.children:
            store_pred(child)
        root.pred = temp
        temp = root


def store_succ(root):
    global temp
    if root:
        for child in root.children:
            store_succ(child)
        if temp is not None:
            temp.succ = root
        temp = root


def store_min(v):
    if v is None:
        return
    else:
        v.min = v.val
        for c in Child[v]:
            store_min(c)
            if c.min < v.min:
                v.min = c.min


def store_all_same(v):
    if v is None:
        return
    else:
        v.Allsame = v.val
        for c in Child[v]:
            store_all_same(c)
            if c.Allsame != v.Allsame:
                v.Allsame = INFINITY


def store_all_same(v):
    if v is None:
        return
    else:
        v.Allsame = v.val
        for c in v.children:
            store_all_same(c)
            if c.Allsame != v.Allsame:
                v.Allsame = float('inf')


def main():
    # T = Node('A',
    #          Node('B'),
    #          Node('C',
    #               Node('E'),
    #               Node('F'),
    #               ),
    #          Node('D')
    #          )
    # T = Node('A',
    #          Node('B'),
    #          Node('C',
    #               Node('E', Node('E'), Node('E')),
    #               Node('F'),
    #               ),
    #          Node('D')
    #          )
    T = Node('a',
             Node('b', Node('e')),
             Node('c',
                  Node('f'),
                  Node('g')),
             Node('d')
             )
    print_tree(T, horizontal=False)
    postorder(T)
    print()
    preorder(T)
    # dfs(T, 'C').gold = 1
    # bfs(T, 'A').gold = 1
    # bfs(T, 'B').gold = 1
    # bfs(T, 'C').gold = 1
    # bfs(T, 'E').gold = 1

    # store_all_same(T)
    # print_tree(T, nameattr="Allsame", horizontal=False)

    # print()
    # postorder_fields(T, 'succ')
    # print('Gold:')
    # print_tree(T, nameattr="gold", horizontal=False)
    # print('Dist:')
    # print_tree(T, nameattr="dist", horizontal=False)


if __name__ == '__main__':
    main()
