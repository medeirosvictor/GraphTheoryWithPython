#!/usr/bin/python
import itertools

from dfs import dfs_cycle

def hierholzer(graph, node):
    graph_nodes = [x for x in graph]
    graph_size = len(graph_nodes)
    graph_edges = []
    for node in graph_nodes:
        for adj in graph[node]:
            graph_edges.append((node, adj))
    print(graph_edges)
    visited_edges = {}
    euler_circuit = [node]
    pointer = 0
    while len(graph_edges) > 0:
        sub_tour = []
        dfs_cycle(graph, euler_circuit[pointer], euler_circuit[pointer], sub_tour, visited_edges)
        print("Cycle found: ", sub_tour)
        if len(sub_tour) != 0:
            euler_circuit = list(itertools.chain(euler_circuit[:pointer+1], sub_tour, euler_circuit[pointer+1:]))
        print("Euler tour at the moment: ", euler_circuit)
        pointer += 1
    print(euler_circuit)
    return euler_circuit