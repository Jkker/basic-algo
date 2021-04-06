class Graph:
    def __init__(self):
        self.vertices = {}

    def printGraph(self):
        """prints adjacency list representation of graaph"""
        for i in self.vertices.keys():
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def addEdge(self, fromVertex, toVertex):
        """adding the edge between two vertices"""
        if fromVertex in self.vertices.keys():
            self.vertices[fromVertex].append(toVertex)
        else:
            self.vertices[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        visited = set()
        queue = []
        visited.add(startVertex)
        queue.append(startVertex)
        while queue:
            vertex = queue.pop(0)
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.add(adjacent_vertex)
        return visited

    def DFS(self, startVertex):
        visited = set()
        stack = []
        visited.add(startVertex)
        stack.append(startVertex)
        while stack:
            vertex = stack.pop()
            visited.add(vertex)
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
        return visited

    def DFS_recur(self):
        visited = {vertex: False for vertex in self.vertices}

        def recur(vertex, parent=None):
            nonlocal has_cycles
            if visited[vertex]:
                has_cycles = True
                return
            else:
                visited[vertex] = True
            for neighbor in G.neighbors(vertex):
                if neighbor != parent:
                    recur(neighbor, vertex)

        for vertex in G:
            if not visited[vertex]:
                recur(vertex)


def longestoutof(graph, Ecost):
    def dfs_recur(vertex):
        vertex.visited = True
        vertex.longestoutof = 0
        for adjacent_vertex in graph[vertex]:
            if not vertex.visited:
                dfs_recur(adjacent_vertex)
                vertex.longestoutof = \
                    max(vertex.longestoutof,
                        adjacent_vertex.longestoutof +
                        Ecost(vertex, adjacent_vertex))

    for vertex in graph:
        if not vertex.visited:
            dfs_recur(vertex)


def longestinto(graph, Ecost):
    for vertex in graph:
        for adjacent_vertex in graph[vertex]:
            adjacent_vertex.in_degree += 1

    queue = []
    for vertex in graph:
        if vertex.in_degree == 0:
            queue.append(vertex)

    while queue:
        vertex = queue.pop(0)
        for adjacent_vertex in graph[vertex]:
            adjacent_vertex.in_degree -= 1
            if adjacent_vertex.in_degree == 0:
                queue.append(adjacent_vertex)
                adjacent_vertex.longestinto = \
                    max(adjacent_vertex.longestinto,
                        vertex.longestinto +
                        Ecost(vertex, adjacent_vertex))


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3
    print(g.BFS(2))
    print(g.DFS(2))
    # print(g.max_distance())
    assert sorted(g.BFS(2)) == [0, 1, 2, 3]
