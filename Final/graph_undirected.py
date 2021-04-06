import networkx as nx
from graph_directed_acyclic import draw_graph


def BFS(graph, startVertex):
    visited = set()
    queue = []
    visited.add(startVertex)
    queue.append(startVertex)
    while queue:
        vertex = queue.pop(0)
        for adjacent_vertex in graph.vertices[vertex]:
            if adjacent_vertex not in visited:
                queue.append(adjacent_vertex)
                visited.add(adjacent_vertex)
    return visited


def DFS(graph, startVertex):
    visited = set()
    stack = []
    visited.add(startVertex)
    stack.append(startVertex)
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        for adjacent_vertex in graph.vertices[vertex]:
            if adjacent_vertex not in visited:
                stack.append(adjacent_vertex)
    return visited


def DFS_recur(graph):
    visited = {vertex: False for vertex in graph}

    def recur(vertex):
        visited[vertex] = True
        print(vertex, end=' ')
        for neighbor in graph.neighbors(vertex):
            if not visited[neighbor]:
                recur(neighbor)

    for vertex in graph:
        if not visited[vertex]:
            recur(vertex)


def cycle_detect_dfs(G):
    visited = {vertex: False for vertex in G}
    has_cycles = False

    def dfs(vertex, parent=None):
        nonlocal has_cycles
        if visited[vertex]:
            has_cycles = True
            return
        else:
            visited[vertex] = True
        for neighbor in G.neighbors(vertex):
            if neighbor != parent:
                dfs(neighbor, vertex)

    for vertex in G:
        if not visited[vertex]:
            dfs(vertex)

    return has_cycles


def find_center(G):
    if cycle_detect_dfs(G):
        raise Exception('Graph has cycles')
    # Store the degrees of all vertices
    degree = {vertex: 0 for vertex in G}
    for u, v in G.edges:
        degree[u] += 1
        degree[v] += 1

    leaves, new_leaves = [], []
    for vertex in G:
        # Add all leaf-like & isolated vertices
        if degree[vertex] == 0 or degree[vertex] == 1:
            leaves.append(vertex)
            degree[vertex] = 0
    count = len(leaves)

    while count < len(G):  # while not all vertices are processed
        vertex = leaves.pop(0)
        for adj in G[vertex]:
            # Chop a leaf by decreasing its neighbor's degree
            degree[adj] -= 1
            if degree[adj] == 1:
                new_leaves.append(adj)  # add newly found leaves
        if not leaves:  # no more leaves to be processed
            count += len(new_leaves)
            leaves = new_leaves
            new_leaves = []

    return leaves


def find_center2(G):
    if cycle_detect_dfs(G):
        raise Exception('Graph has cycles')
    n = len(G)
    degree = {vertex: 0 for vertex in G}

    for u, v in G.edges:
        degree[u] += 1
        degree[v] += 1

    leaves = []
    for v in G:
        if degree[v] == 0 or degree[v] == 1:
            leaves.append(v)
            degree[v] = 0
    count = len(leaves)

    while count < n:
        new_leaves = []
        for v in leaves:
            for neighbor in G[v]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


# Robust BFS Topological Sort w/ Cycle Detection
def topological_sort_bfs(graph):
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] += 1

    blocked, ready = set(), set()
    output = []

    for vertex in graph:
        if in_degree[vertex] == 0:
            ready.add(vertex)
        else:
            blocked.add(vertex)

    while ready:  # while there remains vertices with 0 incoming degree
        vertex = ready.pop()
        output.append(vertex)
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1
            if in_degree[adjacent_vertex] == 0:
                blocked.remove(adjacent_vertex)
                ready.add(adjacent_vertex)

    # Cycles exist if some vertices are not yet processed
    return 'Cycle exists' if blocked else output


def find_largest_k_strong(G):
    # Store the degrees of all vertices
    degree = {vertex: 0 for vertex in G}
    for u, v in G.edges:
        degree[u] += 1
        degree[v] += 1

    least, new_least = [], []
    min_deg = min(degree.values())
    for vertex in G:
        # Add all leaf-like & isolated vertices
        if degree[vertex] == min_deg:
            least.append(vertex)
            degree[vertex] = 0
    print(least)
    count = len(least)

    while count < len(G):  # while not all vertices are processed
        vertex = least.pop(0)
        for adj in G[vertex]:
            # Chop a leaf by decreasing its neighbor's degree
            degree[adj] -= 1
            if degree[adj] <= min_deg:
                new_least.append(adj)  # add newly found leaves
        if not least:  # no more leaves to be processed
            count += len(new_least)
            least = new_least
            new_least = []


def find_largest_k_strong(graph):
    degree = {vertex: 0 for vertex in G}
    for u, v in G.edges:
        degree[u] += 1
        degree[v] += 1

    blocked, least = set(), set()
    output = []
    min_deg = min(degree.values())

    for vertex in graph:
        if degree[vertex] == min_deg:
            least.add(vertex)
        else:
            blocked.add(vertex)

    count = len(least)
    while count < len(G):
        new_least = []
        vertex = least.pop()
        output.append(vertex)
        for adjacent_vertex in graph[vertex]:
            degree[adjacent_vertex] -= 1
            if degree[adjacent_vertex] <= min_deg:
                blocked.remove(adjacent_vertex)
                least.add(adjacent_vertex)

        if not least:  # no more leaves to be processed
            count += len(new_least)
            least = new_least
            min_deg = min(degree.values())

    return least


if __name__ == '__main__':
    # graph_data = {0: [2], 1: [0, 2, 3], 2: [], 3: []}  # (cyclic)
    # graph_data = {0: [1, 3], 1: [2, 3], 2: [3], 3: []}  # (cyclic)
    # graph_data = {0: [], 1: [0, 2, 3], 2: [], 3: []}  # (Tree) 1-vertex center
    # graph_data = {0: [], 1: [0, 2, 3], 2: [4, 5], 3: []}  # 2-vertex center
    # graph_data = {0: [], 1: [0, 2, 3], 2: [3, 4, 5], 3: []}  # (cyclic) 3-vertex center
    graph_data = {0: [1], 1: [2, 3], 2: [3, 0], 3: [0], 5: [0], 6: [5, 0], 7: [1]}

    G = nx.Graph(graph_data)
    print(f'Dict of Lists Representation:\n{nx.to_dict_of_lists(G)}')
    print(f'Vertices:\t{G.nodes}')
    print(f'Edges:\t\t{G.edges}')
    # print(f'Adjacency Matrix:\n{nx.adjacency_matrix(G).todense()}\n')
    print(f'Has Cycles:\t{cycle_detect_dfs(G)}')
    # print(f'Topo BFS:\t{topological_sort_bfs(G)}')
    print(f'k Strong:\t{find_largest_k_strong(G)}')
    # print(f'Center:\t\t{find_center(G)}')
    # print(f'Center (2):\t\t{find_center2(G)}')
    # print(f'Center (nx):\t\t{nx.center(G)}')
    draw_graph(G, show=True)
