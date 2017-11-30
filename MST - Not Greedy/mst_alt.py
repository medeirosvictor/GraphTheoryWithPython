#!/usr/bin/python
from dfs import dfs_cycle
import operator
from graph import Graph

def mst_alt(graph, edges_weights):
    temp_tree = {k: [] for k in graph}
    mst = {}
    print("Edge weights: ", edges_weights)
    for edge in edges_weights:
        print("Inserted edge: ", edge)
        mst[edge] = edges_weights[edge]
        temp_tree[edge[0]].append(edge[1])
        temp_tree[edge[1]].append(edge[0])
        if dfs_cycle(temp_tree, 0):
            max_key = max(mst.items(), key=operator.itemgetter(1))[0]
            print("Removed edge: ", max_key)
            temp_tree[max_key[0]].remove(max_key[1])
            temp_tree[max_key[1]].remove(max_key[0])
            mst.pop(max_key)
        print("Partial MST: ", mst)
    print("Final MST: ", mst)
    print("Peso total da MST obtida: ", sum(mst.values()))
    return mst
