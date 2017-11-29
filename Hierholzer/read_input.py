#!/usr/bin/python

def read_file():
    """Reads input from .txt file and returns graph_size, adj_matrix and adj_list"""

    import os
    import glob

    print('Reading input test file inside sample directory')
    file_path = glob.glob("test/*.txt")
    file = file_path[0]

    adj_matrix = []
    with open(file, 'r') as test_file:
        graph_size = test_file.readline()
        for line in test_file:
            matrix_row = list(map(int, line.split()))
            adj_matrix.append(matrix_row)
    print("Graph size: ", graph_size)
    print("Adjacency Matrix: ", adj_matrix)
    return graph_size, adj_matrix
