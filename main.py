from modules import read_file
from modules import converter
from modules import dfs
from modules import hierholzer

def main():
    graph_size, adj_matrix = read_file()
    graph = converter.matrix_to_list(adj_matrix)
    visited = dfs(graph, 0, [])
    hierholzer(graph, 0)
    print(visited)

if __name__ == '__main__':
    main()
