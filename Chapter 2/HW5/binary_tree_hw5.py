from binary_tree import preorder, postorder, inorder, inorder_fields


class Node:
    def __init__(self, dat, left=None, right=None):
        self.dat = dat  # Assign data
        self.left = left  # Initialize
        self.right = right  # Initialize
        self.ans = None  # Not Initialized


inorder_sum = 0


def store_ans_inorder(root):
    global inorder_sum
    if root:
        store_ans_inorder(root.left)
        inorder_sum += root.val
        root.ans = inorder_sum
        store_ans_inorder(root.right)


if __name__ == '__main__':
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
    store_ans_inorder(Xb)
    inorder(Xb)
    print()
    inorder_fields(Xb, 'ans')
