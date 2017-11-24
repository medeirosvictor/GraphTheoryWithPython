def subtract_edges(graph_1, graph_2):
    for edge_2 in graph_2:
        for edge_1 in graph_1:
            if edge_1 == edge_2:
                graph_1.remove(edge_1)
                temp = (edge_2[1], edge_2[0])
                graph_1.remove(temp)
    updated_graph = dict((x, []) for x, y in graph_1)
    for node in updated_graph:
        for edge in graph_1:
            if edge[0] == node:
                updated_graph[node].append(edge[1])
    return updated_graph