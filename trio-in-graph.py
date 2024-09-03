def trioingraph(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    print(graph)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
trioingraph(n, edges) # [1, 2, 3]