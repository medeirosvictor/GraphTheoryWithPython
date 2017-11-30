#!/usr/bin/python

from read_input import read_file
from converter import matrix_to_list


def main():
    graph_size, adj_matrix = read_file()
    graph = matrix_to_list(adj_matrix)
    print graph


if __name__ == '__main__':
    main()
