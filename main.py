from modules import read_file
from modules import converter
from modules import dfs
from modules import hierholzer
from modules import is_connected
from modules import is_eulerian_graph
from modules import is_semi_eulerian_graph

def main():
    """Read file input"""
    graph_size, adj_matrix = read_file()
    """Convert adjacency matrix to adjacency list and use it as main graph data structure"""
    graph = converter.matrix_to_list(adj_matrix)
    is_connected(graph)
    is_eulerian_graph(graph)
    odd_vertex = is_semi_eulerian_graph(graph)
    start_vertex = 0 if odd_vertex is None else odd_vertex[0]
    print("Euler Tour: ", hierholzer(graph, start_vertex))

if __name__ == '__main__':
    main()
