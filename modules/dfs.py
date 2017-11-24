from subtract_edges import subtract_edges
from converter import list_to_path

def dfs_cycle(graph, node, parent_node, start_node, sub_tour, cycle):
    """Modified DFS to get cycles"""
    start_node = node
    black = []
    visited = []
    visited.append(node)
    found_cyle = False
    while not found_cyle:
        while True:
            for node_adj in graph[node]:
                if ((node, node_adj) not in sub_tour and (node_adj, node) not in sub_tour) and node_adj != parent_node:
                    sub_tour.append((node, node_adj))
                    parent_node = node
                    node = node_adj
                    break
            if node == start_node:
                found_cyle = True
                break
    return sub_tour