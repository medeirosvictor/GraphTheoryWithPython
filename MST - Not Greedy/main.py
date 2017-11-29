#!/usr/bin/python

from read_input import read_file
from converter import matrix_to_list
from hierholzer import hierholzer
from graph import Graph

def main():
    """Read file input
       Convert adjacency matrix to adjacency list and use it as main graph data structure
       Call Hierholzer Algorithm"""

    graph_size, adj_matrix = read_file()
    graph = matrix_to_list(adj_matrix)
    hierholzer(graph, 0)


if __name__ == '__main__':
    main()
