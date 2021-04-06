import copy


def APSP_simple(n, edge_cost):
    path_cost = copy.deepcopy(edge_cost)

    for k in range(n):  # update all path distances by including k as a intermediate vertex
        for i in range(n):
            for j in range(n):
                # Curr cost from i to j > New cost from i to j by going through k
                if path_cost[i][j] > path_cost[i][k] + path_cost[k][j]:
                    path_cost[i][j] = path_cost[i][k] + path_cost[k][j]  # update best cost
    return path_cost


def all_pairs_shortest_path(n, edge_cost, recover_path=None):
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


def two_step_shortest_path(n, edge_cost):
    best = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            best[i][j] = float('inf')
            for k in range(n):
                if best[i][j] > edge_cost[i][k] + edge_cost[k][j]:
                    best[i][j] = edge_cost[i][k] + edge_cost[k][j]
    return best


def first_vertex(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    intermediate = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            if edge_cost[i][j] is not float('-inf'):
                intermediate[i][j] = 0
            else:
                intermediate[i][j] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
                    intermediate[i][j] = k
    return intermediate


def count_edges_in_shortest_path(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    ecount = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            if edge_cost[i][j] is not float('-inf'):
                ecount[i][j] = 1
            else:
                ecount[i][j] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
                    ecount[i][j] = ecount[i][k] + ecount[k][j]
    return ecount


def count_num_of_shortest_path(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    count = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            if pcost[i][j] != float('inf'):
                count[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
                    count[i][j] = count[i][k] * count[k][j]
                elif pcost[i][j] == pcost[i][k] + pcost[k][j]:
                    count += count[i][k] * count[k][j]
    return count


# 8.21 a
def longest_edge(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > max(pcost[i][k], pcost[k][j]):
                    pcost[i][j] = max(pcost[i][k], pcost[k][j])


# 8.21 b
def product_of_edge_cost(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] * pcost[k][j]:
                    pcost[i][j] = pcost[i][k] * pcost[k][j]


def cookies_found(n, edge_cost, cookie):
    pcost = copy.deepcopy(edge_cost)
    found = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            if pcost is not float('-inf'):
                found[i][j] = cookie[i] + cookie[j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
                    found[i][j] = found[i][k] - cookie[k] + found[k][j]


def cookie_monster_APSP(n, edge_cost, cookie):
    pcost = copy.deepcopy(edge_cost)
    found = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            if pcost is not float('-inf'):
                found[i][j] = cookie[i] + cookie[j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
                    found[i][j] = found[i][k] - cookie[k] + found[k][j]
                elif pcost[i][j] == pcost[i][k] + pcost[k][j]:
                    found[i][j] = max(found[i][j],
                                      found[i][k] - cookie[k] + found[k][j])


def cookied_supergraph(n, edge_cost, cookie):
    pcost = [[float('inf')] * 2 * n] * 2 * n
    for i in range(n):
        if cookie[i] != 0:
            pcost[i][i + n] = 0
        for j in range(n):
            pcost[i][j] = edge_cost[i][j]
            pcost[i + n][j + n] = edge_cost[i][j]

    for k in range(2 * n):
        for i in range(2 * n):
            for j in range(2 * n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
    return pcost


def cookied_discern(n, edge_cost, cookie):
    pcost = copy.deepcopy(edge_cost)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
    best = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            if cookie[i] + cookie[j] != 0:
                best[i][j] = pcost[i][j]
                continue
            best[i][j] = float('inf')
            for k in range(n):
                if cookie[k] != 0 and best[i][j] > pcost[i][k] + pcost[k][j]:
                    best[i][j] = pcost[i][k] + pcost[k][j]
    return best


def dijkstra_SSSP(p, s):
    pass


def shopping_SSSP(n, edge_cost, s, S):
    pcost = [[float('inf')] * 2 * n] * 2 * n
    for i in range(n):
        if i in S:
            pcost[i][i + n] = 0
        for j in range(n):
            pcost[i][j] = edge_cost[i][j]
            pcost[i + n][j + n] = edge_cost[i][j]

    return dijkstra_SSSP(pcost, s)


def even_number_APSP(n, edge_cost):
    two_edge_sp = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            two_edge_sp[i][j] = float('inf')
            for k in range(n):
                if two_edge_sp[i][j] > edge_cost[i][k] + edge_cost[k][j]:
                    two_edge_sp[i][j] = edge_cost[i][k] + edge_cost[k][j]
    pcost = [[float('inf')] * 2 * n] * 2 * n
    for i in range(n):
        for j in range(n):
            pcost[i][j] = edge_cost[i][j]
            pcost[i + n][j + n] = edge_cost[i][j]

    for k in range(2 * n):
        for i in range(2 * n):
            for j in range(2 * n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    pcost[i][j] = pcost[i][k] + pcost[k][j]
    return pcost


def even_number_APSP2(n, edge_cost):
    pcost = copy.deepcopy(edge_cost)
    for k in range(n):
        even = False
        for i in range(n):
            for j in range(n):
                if pcost[i][j] > pcost[i][k] + pcost[k][j]:
                    if even:
                        pcost[i][j] = pcost[i][k] + pcost[k][j]
                        even = not even
