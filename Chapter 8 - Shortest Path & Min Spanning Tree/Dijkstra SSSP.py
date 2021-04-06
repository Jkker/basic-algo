DIJKSTRA(graph G, start vertex s, destination vertex d):
1 -  let H = min heap data structure, initialized with 0 and s
	   #(0 indicates the distance from start vertex s)
2 -  while H is non-empty:
3 -    remove the first node and cost of H, call it U and cost
4 -    if U has been previously explored:
5 -      continue # skip nodes that are processed already
6 -    mark U as explored
7 -    if U is d:
8 -      return cost # total cost from start to destination vertex
9 -    for each edge(U, V): c=cost of edge(U,V) # for V in graph[U]
10 -     if V explored:
11 -       go to next V in line 9
12 -     total_cost = cost + c
13 -     add (total_cost,V) to H