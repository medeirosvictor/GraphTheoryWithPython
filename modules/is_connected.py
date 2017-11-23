def is_connected(graph):
    for node in graph:
        if len(graph[node]) == 0:
            print("The graph is not connected.")
            input("exit")
            return False
