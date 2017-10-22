def read_input():
    import os

    file_path = input('Enter path to sample file...')
    assert os.path.exists(file_path), "File not found at, " + str(file_path)

    AdjMatrix = []
    with open(file_path, 'r') as sample_file:
        graph_size = sample_file.readline()
        for line in sample_file:
            matrix_row = list(map(int, line.split()))
            AdjMatrix.append(matrix_row)
    return graph_size, AdjMatrix