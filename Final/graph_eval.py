def graph_eval(graph):
    visited, stack = [], []

    def depth_first_search(start_vertex):
        visited[start_vertex] = 1
        for adjacent_vertex in graph[start_vertex]:
            if not visited[adjacent_vertex]:
                depth_first_search(adjacent_vertex)

        stack.append(start_vertex)

    for vertex in graph:
        if not visited[vertex]:
            depth_first_search(vertex)

    return reversed(stack)


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
    elif type(root.dat) is int:
        return root.dat
    else:
        root.dat = exp_eval(root.dat, tree_eval(root.left), tree_eval(root.right))
        return root.dat
