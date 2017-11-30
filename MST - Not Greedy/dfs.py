#!/usr/bin/python


def dfs_cycle(graph, node, start_node, sub_tour, visited):
    """Modified DFS to get cycles"""

    for node_adj in graph[node]:
        if (node_adj, node) or (node, node_adj) not in visited:
            visited[(node_adj, node)] = visited[(node, node_adj)] = True
            sub_tour.append(node_adj)
            if node == start_node:
                return
        else:
            dfs_cycle(graph, node_adj, start_node, sub_tour, visited)
