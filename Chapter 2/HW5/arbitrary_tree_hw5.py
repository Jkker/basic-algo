from arbitrary_tree import preorder, postorder, postorder_fields, preorder_fields


class Node:
    def __init__(self, dat, *children):
        self.dat = dat
        self.children = list(children)
        self.ans = None


preorder_sum = 0


def store_ans_preorder(root):
    global preorder_sum
    if root:
        preorder_sum += root.val
        root.ans = preorder_sum
        for child in root.children:
            store_ans_preorder(child)


# Global Variable
postorder_sum = 0


def store_ans_postorder(root):
    global postorder_sum
    if root:
        for child in root.children:
            store_ans_postorder(child)
        postorder_sum += root.val
        root.ans = postorder_sum


dat_sum = 0  # Global Variable


def store_ans_npre_at_post(root):
    def sum_all_dat(root):
        global dat_sum
        if root:
            dat_sum += root.val
            for child in root.children:
                sum_all_dat(child)

    def store_ans_at_post(root):
        global dat_sum
        if root:
            dat_sum -= root.val
            for child in root.children:
                store_ans_at_post(child)
            root.ans = dat_sum

    sum_all_dat(root)
    store_ans_at_post(root)


pre_npost_sum = 0  # Global Variable


def store_ans_pre_npost(root):
    global pre_npost_sum
    pre_npost_sum += root.val
    for child in root.children:
        store_ans_pre_npost(child)
    root.ans = pre_npost_sum
    pre_npost_sum -= root.val


if __name__ == '__main__':
    N = Node(0,
             Node(1),
             Node(2,
                  Node(4,
                       Node(6),
                       Node(7))),
             Node(3,
                  Node(5)))

    store_ans_pre_npost(N)

    preorder(N)
    print()
    preorder_fields(N, 'ans')
