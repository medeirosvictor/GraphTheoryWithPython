#!/usr/bin/python

from read_input import read_file
from converter import matrix_to_list
from MST_ALT import mst_alt
from graph import Graph


def main():
    graph_size, adj_matrix = read_file()
    graph = matrix_to_list(adj_matrix)
    print(graph)
    graph = Graph(graph)
    print("Edges: ", graph.edges)
    print("Nodes: ", graph.nodes)
    mst_alt(graph)


if __name__ == '__main__':
    main()
