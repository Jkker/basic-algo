def topological_sort_bfs(graph):
    in_degree = [0] * len(graph)
    for vertex, adj_list in enumerate(graph):
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] += 1

    blocked, ready = set(), set()
    output = []

    for vertex, adj_list in enumerate(graph):
        if in_degree[vertex] == 0:
            ready.add(vertex)
        else:
            blocked.add(vertex)

    while ready:  # ready is not empty
        vertex = ready.pop()
        output.append(vertex)
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1
            if in_degree[adjacent_vertex] == 0:
                blocked.remove(adjacent_vertex)
                ready.add(adjacent_vertex)

    if blocked:  # blocked is not empty
        raise Exception('A cycle exists')
    else:
        return output


def topological_sort_dfs(graph):
    stack = []
    visited = [None] * len(graph)

    def depth_first_search(start_vertex):
        visited[start_vertex] = True
        for adjacent_vertex in graph[start_vertex]:
            if not visited[adjacent_vertex]:
                depth_first_search(adjacent_vertex)

        stack.append(start_vertex)

    for vertex, adj_list in enumerate(graph):
        if not visited[vertex]:
            depth_first_search(vertex)

    return list(reversed(stack))


def find_center(graph):
    for vertex in graph:
        vertex.in_degree = len(graph[vertex])

    queue = []
    visited = 0

    for vertex in graph:
        if vertex.in_degree <= 1:
            queue.append(vertex)

    while queue is not None and visited != len(graph) - 1:
        vertex = queue.pop(0)
        visited += 1
        for adjacent_vertex in graph[vertex]:
            adjacent_vertex.in_degree -= 1
            if adjacent_vertex.in_degree == 1:
                queue.append(adjacent_vertex)

    return queue[0]


def find_center2(graph):
    in_degree = {}
    for vertex, adj in enumerate(graph):
        in_degree[vertex] = len(adj)
    queue = []
    visited = 0

    for vertex, adj in enumerate(graph):
        if in_degree[vertex] <= 1:
            queue.append(vertex)

    while queue is not None and visited != len(graph) - 1:
        vertex = queue.pop(0)
        visited += 1
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1
            if in_degree[adjacent_vertex] == 1:
                queue.append(adjacent_vertex)

    return queue[0]


if __name__ == '__main__':
    # graph = [[1], [0, 2, 3], [1], [1]]
    graph = [[], [0, 2, 3], [], []]
    print(topological_sort_bfs(graph))
    print(topological_sort_dfs(graph))
    print(find_center2(graph))
