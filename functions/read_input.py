def read_input():
    """Reads input from .txt file and returns graph_size, adj_matrix and adj_list"""

    import os

    file_path = input('Enter path to sample file...')
    assert os.path.exists(file_path), "File not found at, " + str(file_path)

    adj_matrix = []
    with open(file_path, 'r') as sample_file:
        graph_size = sample_file.readline()
        for line in sample_file:
            matrix_row = list(map(int, line.split()))
            adj_matrix.append(matrix_row)

    return graph_size, adj_matrix
