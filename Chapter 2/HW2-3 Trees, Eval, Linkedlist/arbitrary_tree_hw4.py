from arbitrary_tree import preorder, postorder, postorder_fields, preorder_fields


class Node:
    def __init__(self, data, *children):
        self.val = data  # Assign data
        self.children = list(children)
        self.postID = None
        self.preID = None


id = 0


def store_ids(root):
    global id
    if root:
        root.preID = id
        for child in root.children:
            id += 1
            store_ids(child)
        root.postID = id


if __name__ == '__main__':
    X = Node(1,
             Node(2),
             Node(3,
                  Node(5),
                  Node(6)),
             Node(4))
    preorder(X)
    print()
    postorder(X)
    print()
    store_ids(X)
    preorder_fields(X, 'postID')
