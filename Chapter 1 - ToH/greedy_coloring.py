def greedy_coloring_1(G):
    uncolored_vertices = []
    colorable_vertices = G.Vertices.copy()
    current_color = 1
    while colorable_vertices:
        # color the current vertex & remove its neighbors
        for current_vertex in colorable_vertices:
            colorable_vertices.remove(current_vertex)
            G.Colors[current_vertex] = current_color
            # prevent neighbors of the current vertex to be colored in this round
            for neighbors in G.Adj[current_vertex]:
                if neighbors in colorable_vertices:
                    colorable_vertices.remove(neighbors)
                    uncolored_vertices.append(neighbors)
        # move all remnants to colorable_vertices
        while uncolored_vertices:
            colorable_vertices.append(uncolored_vertices.pop())
        # prepare the new color for next round
        current_color += 1


def greedy_coloring_2(G):
    for vertex in G.Vertices:
        neighbors = G.Adj[vertex]
        num_of_neighbors = len(neighbors)
        available_colors = [True] * num_of_neighbors
        for index, neighbor in enumerate(G.Adj[vertex]):
            if G.Color[neighbor]:  # Check if neighbor is colored
                available_colors[index] = False  # Assign False if colored

        color = available_colors.index(True)  # Returns the index of the first available color
        if not color:
            color = len(available_colors)  # Assign a new color
        G.Color[vertex] = color
