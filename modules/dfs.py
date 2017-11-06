def dfs(graph, vertex, visited):

    if vertex not in visited:
        visited.append(vertex)
        for vertex_adj in graph[vertex]:
            dfs(graph, vertex_adj, visited)
    return visited
