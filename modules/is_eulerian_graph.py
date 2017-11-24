def is_eulerian_graph(graph):
    for node in graph:
        if len(graph[node]) % 2 != 0:
            response = raw_input("The graph is not eulerian.")
            exit()
