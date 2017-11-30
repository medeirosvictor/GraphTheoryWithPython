#!/usr/bin/python
from dfs import dfs_cycle
import operator
from graph import Graph

def mst_alt(graph, edges_weights):
    mst = {k: [] for k in graph}
    temp_tree = {}
    print("Edge weights: ", edges_weights)
    for edge in edges_weights:
        print("Inserted edge: ", edge)
        temp_tree[edge] = edges_weights[edge]
        mst[edge[0]].append(edge[1])
        mst[edge[1]].append(edge[0])
        if dfs_cycle(mst, 0):
            max_key = max(temp_tree.items(), key=operator.itemgetter(1))[0]
            print("Removed edge: ", temp_tree[max_key])
            mst[max_key[0]].remove(max_key[1])
            mst[max_key[1]].remove(max_key[0])
            temp_tree.pop(max_key)
        print("Partial MST: ", mst)
    print("Final MST: ", temp_tree)
    return mst
