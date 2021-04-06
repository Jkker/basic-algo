class Node:
    def __init__(self, data=None, left=None, right=None):
        self.dat = data  # Assign data
        self.left = left  # Initialize
        self.right = right  # Initialize


class Tree:
    def __init__(self, root):
        self.root = root


def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')


def inorder_fields(root, field):
    if root:
        inorder_fields(root.left, field)
        print(getattr(root, field), end=' ')
        inorder_fields(root.right, field)


def clone(v):
    lookup = {}

    def clone_pointers(v):
        if v is None: return None
        lookup[v] = newBinVert(v.val)
        lookup[v].left = clone_pointers(v.left)
        lookup[v].right = clone_pointers(v.right)
        return lookup[v]

    return lookup[v]


if __name__ == '__main__':
    X = Node(51,
             Node(6,
                  Node(3,
                       None,
                       Node(5)),
                  Node(14, Node(17, None, Node(11)))),
             None)
    preorder(X)
    print()
    inorder(X)
    print()
    postorder(X)
