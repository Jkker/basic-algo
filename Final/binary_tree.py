class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data  # Assign data
        self.left = left  # Initialize
        self.right = right  # Initialize

    def __str__(self):
        def _build_tree_string(root, curr_index, index=False, delimiter='-'):
            if root is None:
                return [], 0, 0, 0

            line1 = []
            line2 = []
            if index:
                node_repr = '{}{}{}'.format(curr_index, delimiter, root.val)
            else:
                node_repr = str(root.val)

            new_root_width = gap_size = len(node_repr)

            # Get the left and right sub-boxes, their widths, and root repr positions
            l_box, l_box_width, l_root_start, l_root_end = \
                _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
            r_box, r_box_width, r_root_start, r_root_end = \
                _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

            # Draw the branch connecting the current root node to the left sub-box
            # Pad the line with whitespaces where necessary
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(' ' * (l_root + 1))
                line1.append('_' * (l_box_width - l_root))
                line2.append(' ' * l_root + '/')
                line2.append(' ' * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0

            # Draw the representation of the current root node
            line1.append(node_repr)
            line2.append(' ' * new_root_width)

            # Draw the branch connecting the current root node to the right sub-box
            # Pad the line with whitespaces where necessary
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append('_' * r_root)
                line1.append(' ' * (r_box_width - r_root + 1))
                line2.append(' ' * r_root + '\\')
                line2.append(' ' * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1

            # Combine the left and right sub-boxes with the branches drawn above
            gap = ' ' * gap_size
            new_box = [''.join(line1), ''.join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
                r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
                new_box.append(l_line + gap + r_line)

            # Return the new box, its width and its root repr positions
            return new_box, len(new_box[0]), new_root_start, new_root_end

        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


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
    print(X)
    preorder(X)
    print()
    inorder(X)
    print()
    postorder(X)
