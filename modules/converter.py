def matrix_to_list(adj_matrix):
    """Converts Adjacency Matrix of graph to it's Adjacency List"""

    adj_list = {}
    for i, vertex in enumerate(adj_matrix):
        vertex_adj = []
        for j, connected_to in enumerate(vertex):
            if connected_to:
                vertex_adj.append(j)
                adj_list[i] = vertex_adj

    return adj_list
