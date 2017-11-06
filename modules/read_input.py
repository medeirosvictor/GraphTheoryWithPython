def read_file():
    """Reads input from .txt file and returns graph_size, adj_matrix and adj_list"""

    import os

    option = input('1. Use default test file\n2. Use custom test file...\n')
    if option == '1':
        file_path = os.path.join(os.path.dirname(__file__), '..', 'sample', 'input.txt')
    else:
        file_path = input('Enter path to file...\n')
    assert os.path.exists(file_path), "File not found at, " + str(file_path)

    adj_matrix = []
    print('Reading sample file...')
    with open(file_path, 'r') as sample_file:
        graph_size = sample_file.readline()
        for line in sample_file:
            matrix_row = list(map(int, line.split()))
            adj_matrix.append(matrix_row)
    print("Graph size and Adjacency matrix computed...")
    return graph_size, adj_matrix
