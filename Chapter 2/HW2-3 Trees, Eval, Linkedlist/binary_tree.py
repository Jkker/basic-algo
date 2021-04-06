class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data  # Assign data
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


leaf = 'leaf'


def exp_eval(op, l, r):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    elif op == '*':
        return l * r
    elif op == '/':
        return l / r
    else:
        raise Exception('Unexpected Operator:', op)


def tree_eval(root):
    if root is None:
        return 0
    elif type(root.val) is int:
        return root.val
    else:
        root.val = exp_eval(root.val, tree_eval(root.left), tree_eval(root.right))
        return root.val


def preorder_parent(root, parent):
    if root:
        if parent:
            print((root.val, parent.val), end=' ')
        else:
            print((root.val, None), end=' ')
        preorder_parent(root.right, parent)
        preorder_parent(root.left, root)


def postorder_parent(root, parent):
    # Actually an inorder traversal gives postorder output
    # for the original arbitrary tree
    if root:
        postorder_parent(root.left, root)
        if parent:
            print((root.val, parent.val), end=' ')
        else:
            print((root.val, None), end=' ')
        postorder_parent(root.right, parent)


# ('F', 'B') ('G', 'B') ('B', 'A') ('C', 'A') ('D', 'A') ('E', 'A') ('A', None)

if __name__ == '__main__':
    S = Node('A',
             Node('B',
                  Node('F',
                       None,
                       Node('G')),
                  Node('C',
                       None,
                       Node('D',
                            None,
                            Node('E')
                            )
                       )
                  )
             )
    Xb = Node(1,
              Node(2,
                   None,
                   Node(3,
                        Node(5,
                             None,
                             Node(6)
                             ),
                        Node(4)
                        )
                   ))
    exp = Node('-',
               Node('*',
                    Node(2),
                    Node(3)),
               Node(6))
    # print('Postorder: ')
    # postorder(Xb)
    # print('\nExpected Result: \nF G B C D E A')
    # print('Inorder')
    # inorder(S)
    # print('\nPost order Parent (Actual Inorder)')
    # postorder_parent(S, None)
    # print()
    print(tree_eval(exp))
    postorder(exp)
# ('F', 'B') ('G', 'B') ('B', 'A') ('C', 'A') ('D', 'A') ('E', 'A') ('A', None)
