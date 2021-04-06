Edge *current;

start[v]=clock;                             //We are going to classify the edges by the time they were visited
clock++;
visited[v]=TRUE;

current=Gr->stpoint[v];

while (current){
    w=current->vertex;

    if (!visited[w]) {
        printf("%d %d: Tree edge\n",v,w);       //If w is not visited then mark v-w as a tree edge
        if(!current)
            Traverse(Gr, w);
    }
    else{

        if((start[v] > start[w]) && (end[v] < end[w]))      //v was visited after w
            printf("%d %d: Back edge\n",v,w);
        else if ((start[v] < start[w]) && (end[v] > end[w]))    //v was visited before w
            printf("%d %d: Forward edge\n",v,w);
        else if ((start[v] > start[w]) && (end[v] > end[w]))    //
            printf("%d %d: Cross edge\n",v,w);

    }
    end[v]=clock;
    clock++;
    current=current->next;
 }

}



DFS-Visit(u)         ▷ with edge classification. G must be a directed graph

1.        color[u] ← GRAY
2.        time ← time + 1
3.        d[u] ← time
4.        for each vertex v adjacent to u
5.            do if color[v] ← BLACK
6.                then if d[u] < d[v]
7.                            then Classify (u, v) as a forward edge
8.                            else Classify (u, v) as a cross edge
9.                        if color[v] ← GRAY
10.                            then Classify (u, v) as a back edge
11.                       if color[v] ← WHITE
12.                            then π[v] ← u
13.                                 Classify (u, v) as a tree edge
14.                                 DFS-Visit(v)
15.        color[u] ← BLACK
16.        time ← time + 1
17.        f[u] ← time