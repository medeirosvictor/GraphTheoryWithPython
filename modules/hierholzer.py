from subtract_edges import subtract_edges
from is_not_null import is_not_null
from dfs import dfs_cycle
from converter import list_to_path
from collections import OrderedDict

def hierholzer(graph, node):
    euler_tour = []
    parent_node = node
    start_node = node
    callback = [False]
    T = []
    cycle = dfs_cycle(graph, node, parent_node, start_node, T, callback)
    if not cycle:
        print("Graph is acyclic")
        return euler_tour
    print("Cycle found: ", cycle)
    euler_tour = cycle + euler_tour
    print("Eulerian Tour at the moment: ", euler_tour)
    graph_list = []
    for key in graph:
        for value in graph.get(key):
            temp = (key, value)
            graph_list.append(temp)
    graph = subtract_edges(graph_list, cycle)
    while is_not_null(graph):
        check = False
        for node in graph:
            if len(graph[node]) > 0:
                check = True
                current_node = node
                break
        if not check:
            print("Graph is not eulerian")
            return False
        callback = [False]
        cycle = dfs_cycle(graph, current_node, current_node, current_node, [], callback)
        print("Cycle found: ", cycle)
        if not cycle:
            return euler_tour
        last_values = [t[1] for t in euler_tour]
        for i in range(len(last_values)):
            if last_values[i] == current_node:
                euler_tour[i+1:i] = cycle
                break
        print("Eulerian Tour at the moment: ", euler_tour)
        graph_list = []
        for key in graph:
            for value in graph.get(key):
                temp = (key, value)
                graph_list.append(temp)
        graph = subtract_edges(graph_list, cycle)

    return euler_tour
    