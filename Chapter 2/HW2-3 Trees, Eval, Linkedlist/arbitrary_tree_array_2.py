V = [0, 1, 2, 3, 4, 5, 6, 7]
Child = [[1, 2, 3], [], [4], [5], [6, 7], [], [], []]


def postorder(root):
    global Child
    for child in Child[root]:
        postorder(child)
    print(root, end=' ')


def find_root(Vertices):
    global Child
    mark = [True] * len(V)
    for v in Vertices:
        for c in Child[v]:
            mark[c] = False
    return mark.index(True)


if __name__ == '__main__':
    # postorder(0)
    print(find_root(V))
