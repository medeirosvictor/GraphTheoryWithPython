def is_connected(graph):
    if graph:
        for node in graph:
            if len(graph[node]) == 0:
                response = raw_input("The graph is not connected.")
                exit()
    else:
        response = raw_input("Error: The graph has no edges")
        exit()