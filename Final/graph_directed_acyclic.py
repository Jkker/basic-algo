import copy
import math
import heapq as priority_q  # Priority Queue ADT
from utilities.PriorityQueue import PriorityQueue
import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def draw_graph(G, show=True, weight=False):
    matplotlib.use('TkAgg')
    if not weight:
        nx.draw_networkx(G, with_labels=True, node_color="c", edge_color="k", font_size=8)
    else:
        pos = nx.spring_layout(G, k=5 / math.sqrt(G.order()))  # pos = nx.nx_agraph.graphviz_layout(G)
        nx.draw_networkx(G, pos, node_color="c", edge_color="k")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.draw()
    plt.savefig("graph.jpg")
    if show:
        plt.show()


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


# Robust DFS Topological Sort w/ Cycle Detection
def topological_sort_dfs(graph):
    stack = []
    started = {vertex: False for vertex in graph}
    finished = {vertex: False for vertex in graph}

    def depth_first_search(start_vertex):
        started[start_vertex] = True  # preorder marking
        for adjacent_vertex in graph[start_vertex]:
            if not started[adjacent_vertex]:  # advance on unprocessed vertices
                depth_first_search(adjacent_vertex)
            elif not finished[adjacent_vertex]:  # if the processing is not finished
                print('Topological Sort DFS: Cycle exists')
                # raise Exception('Cycle Exists')
        stack.append(start_vertex)
        finished[start_vertex] = True  # postorder marking

    # Initiate DFS on every vertex that is not started
    for vertex in graph:
        if not started[vertex]:
            depth_first_search(vertex)

    return list(reversed(stack))


# Stores in dist the number of edges in the longest path
# that runs from one of D's root-like vertices to v
def store_distance_to_root(graph):
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] += 1

    blocked, ready = set(), set()
    dist = {vertex: 0 for vertex in graph}

    for vertex in graph:
        if in_degree[vertex] == 0:
            ready.add(vertex)
        else:
            blocked.add(vertex)

    while ready:  # ready is not empty
        vertex = ready.pop()

        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] -= 1
            if dist[adjacent_vertex] <= dist[vertex]:
                dist[adjacent_vertex] = dist[vertex] + 1
            if in_degree[adjacent_vertex] == 0:
                blocked.remove(adjacent_vertex)
                ready.add(adjacent_vertex)

    if blocked:  # blocked is not empty
        return 'Cycle exists'
    else:
        return dist


def cycle_detect_dfs(graph):
    visited = {vertex: False for vertex in graph}
    in_path = {vertex: False for vertex in graph}
    has_cycles = False

    def dfs(vertex):
        nonlocal has_cycles
        visited[vertex] = True
        in_path[vertex] = True
        for adj in graph.neighbors(vertex):
            if in_path[adj]:
                has_cycles = True
                return
            elif not visited[adj]:
                dfs(adj)
        in_path[vertex] = False

    for vertex in graph:
        if not visited[vertex]:
            dfs(vertex)
    return has_cycles


def graph_is_tree(graph):
    def dfs(vertex):
        if visited[vertex]:
            print(f'\tVertex {vertex} has more than 1 parent')
            return False
        visited[vertex] = True
        for adj in graph.neighbors(vertex):
            res = dfs(adj)
            if res is False:
                return res
        return True

    visited = {vertex: False for vertex in graph}
    in_degree = {vertex: 0 for vertex in graph}
    num_of_roots = 0
    for vertex in graph:  # Compute incoming degrees
        for adjacent_vertex in graph[vertex]:
            in_degree[adjacent_vertex] += 1
    for vertex in graph:  # Find root-like vertices
        if in_degree[vertex] == 0:
            num_of_roots += 1
            root = vertex
    # Check if a there is exactly one root-like vertex
    if num_of_roots > 1:
        print('\tFound more than 1 root-like vertex')
        return False
    elif num_of_roots < 1:
        print('\tNo root like vertex found')
        return False
    # Check if a vertex has more than 1 parent
    if not dfs(root):
        return False
    # Check disconnected components
    for vertex in graph:
        if not visited[vertex]:
            print('\tFound disconnected component')
            return False


def FW_APSP(n, edge_cost, recover_path=None):
    path_cost = copy.deepcopy(edge_cost)  # not necessary in Python
    # Stores intermediate vertex on a best path
    # Initialize to -1 else 0 if no edge exists
    intermediate = [[-1 if cost == float('inf') else 0 for cost in _] for _ in edge_cost]

    for k in range(n):  # update all path distances by including k as a intermediate vertex
        for i in range(n):
            for j in range(n):
                # Curr cost from i to j > New cost from i to j by going through k
                if path_cost[i][j] > path_cost[i][k] + path_cost[k][j]:
                    path_cost[i][j] = path_cost[i][k] + path_cost[k][j]  # update best cost
                    intermediate[i][j] = k  # store the most recently used intermediate vertex on a best path

    # Recovers the best path from i to j
    def path_recovery(i, j):
        # DFS traverses the hidden binary tree starting with root [i][j]
        def list_path(i, j):
            k = intermediate[i][j]
            if k == 0:  # best path from i to j is the edge (i, j)
                print(i, end=' -> ')  # output the first vertex
            else:
                list_path(i, k)  # path's vertices from i to k
                list_path(k, j)  # path's vertices from k to j

        if intermediate[i][j] != -1:
            print(f'FW Shortest path from {i} to {j}:', end='\t')
            list_path(i, j)
            print(j)  # output the last vertex
        else:
            print('FW No path exists from', i, 'to', j)

    if recover_path:
        path_recovery(recover_path[0], recover_path[1])
    return path_cost


def FW_APSP_simple(n, edge_cost):
    path_cost = copy.deepcopy(edge_cost)

    for k in range(n):  # update all path distances by including k as a intermediate vertex
        for i in range(n):
            for j in range(n):
                # Curr cost from i to j > New cost from i to j by going through k
                if path_cost[i][j] > path_cost[i][k] + path_cost[k][j]:
                    path_cost[i][j] = path_cost[i][k] + path_cost[k][j]  # update best cost
    return path_cost


# Return the cost of the shortest path between vertices start and end
def Dijkstra_SSSP_single_destination(graph, start, end):
    queue = [(0, start)]  # cost from start node,end node
    visited = set()
    while queue:  # is not empty
        (cost, vertex) = priority_q.heappop(queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == end:
            return cost
        for neighbor, neighbor_cost in graph[vertex]:
            if neighbor in visited:
                continue
            next_cost = cost + neighbor_cost
            priority_q.heappush(queue, (next_cost, neighbor))
    return -1


def Dijkstra_SSSP_all_destination(graph, src, edge_cost):
    dist_to, parent_of = {}, {}

    for vertex in graph:
        dist_to[vertex] = float('inf')
        parent_of[vertex] = -1
    dist_to[src] = 0
    Q = PriorityQueue()
    Q.insert((0, src))  # (dist from src, vertex)

    while not Q.isEmpty():
        vertex = Q.pop_min()  # Returns vertex with the min dist from source
        # Update the distance of all the neighbors of v and
        # if their prev dist was INFINITY then push them in queue
        for neighbor in graph.neighbors(vertex):
            new_dist = dist_to[vertex] + edge_cost[vertex][neighbor]
            if dist_to[neighbor] > new_dist:
                if dist_to[neighbor] == float('inf'):
                    Q.insert((new_dist, neighbor))
                else:
                    Q.reduce_key((dist_to[neighbor], neighbor), new_dist)
                dist_to[neighbor] = new_dist
                parent_of[neighbor] = vertex

    [print(f'Min dist from {src} to {v}: {dist_to[v]}') for v in graph]
    return dist_to


# Robust DFS Topological Sort w/ Cycle Detection
def store_gold(graph):
    stack = []
    started = {vertex: False for vertex in graph}
    finished = {vertex: False for vertex in graph}

    def dfs(start_vertex):
        started[start_vertex] = True  # preorder marking
        for adjacent_vertex in graph[start_vertex]:
            if not started[adjacent_vertex]:  # advance on unprocessed vertices
                dfs(adjacent_vertex)
            elif not finished[adjacent_vertex]:  # if the processing is not finished
                print('Topological Sort DFS: Cycle exists')
                # raise Exception('Cycle Exists')
        stack.append(start_vertex)
        finished[start_vertex] = True  # postorder marking

    # Initiate DFS on every vertex that is not started
    for vertex in graph:
        if not started[vertex]:
            dfs(vertex)

    return list(reversed(stack))


def curley_q(graph, r):
    time = 0
    started, finished = {}, {}
    parent = {}
    order = []
    is_curly_q = True

    def dfs(v, p=None):
        nonlocal time, is_curly_q
        parent[v] = p
        time += 1
        started[v] = time

        for n in graph[v]:
            if n not in parent:
                dfs(n, v)
            elif n not in finished:
                pass
            elif started[v] < started[n]:
                is_curly_q = False
            else:
                is_curly_q = False

        time += 1
        finished[v] = time
        order.append(v)

    dfs(r)
    print('YES' if is_curly_q else 'NO')
    return is_curly_q


def main():
    gc = {0: [2], 1: [0, 3], 2: [1], 3: []}  # Cyclic
    gac = {0: [1, 3], 1: [2, 3], 2: [3], 3: []}  # Acyclic
    gt = {0: [], 1: [0, 2, 3], 2: [], 3: []}  # Tree
    gdc = {0: [], 1: [0, 2, 3], 2: [], 3: [], 4: [5], 5: [4]}  # Tree w/ disconnected cyclic component
    gw = [(0, 1, 2), (0, 3, 3), (1, 2, 5), (1, 3, 9), (2, 3, 1)]
    gw2 = [(0, 1, 2), (0, 3, 3), (1, 2, 5), (1, 3, 9), (2, 3, 1), (0, 4, 10), (3, 4, 2)]
    # cq = {0: [1], 1: [2, 3], 2: [0], 3: [4], 4: [1, 0]}
    # cq = {0: [1, 2], 1: [3], 2: [3], 3: [4]}
    G = nx.DiGraph()
    G.add_weighted_edges_from(gw2)

    print(f'Dict Representation:\t{nx.to_dict_of_lists(G)}')
    print(f'Vertices:\t{G.nodes}')
    print(f'Edges:\t\t{G.edges}')
    # print(f'Adjacency Matrix:\n{nx.adjacency_matrix(G).todense()}\n')
    print(f'Has Cycles:\t{cycle_detect_dfs(G)}')
    print(f'Is Tree:\t{graph_is_tree(G)}')

    # print(f'Topological Sort BFS: {topological_sort_bfs(G)}')
    # print(f'Topological Sort DFS: {topological_sort_dfs(G)}')

    # print(store_distance_to_root(G))
    # print(f'Is CurlyQ: {curley_q(G, 0)}')
    print(f'Adjacency Matrix:\n{nx.adjacency_matrix(G)}\n')
    adj = [[float('inf') if i == 0 else i for i in j] for j in nx.adjacency_matrix(G).todense().tolist()]
    print(f'FW APSP Cost: \n{np.asmatrix(FW_APSP(len(G), adj, recover_path=(0, 4)))}')
    # Dijkstra_SSSP_all_destination(G, 1, adj)

    draw_graph(G, show=True, weight=True)


if __name__ == '__main__':
    main()
