#!/usr/bin/python
from dfs import dfs_cycle
import operator
from test import kappa
from graph import Graph


def mst_alt(graph, edges_weights):
    temp_tree = {k: [] for k in graph}
    mst = {}
    for edge in edges_weights:
        print"Inserted edge: ", edge
        mst[edge] = edges_weights[edge]
        temp_tree[edge[0]].append(edge[1])
        temp_tree[edge[1]].append(edge[0])
        if dfs_cycle(temp_tree, 0):
            cycle = kappa(mst)
            heaviest = cycle[0]
            for x in cycle:
                if edges_weights[heaviest] < edges_weights[x]:
                    heaviest = x
            temp_tree[heaviest[0]].remove(heaviest[1])
            temp_tree[heaviest[1]].remove(heaviest[0])
            mst.pop(heaviest)
            print"Removed edge: ", heaviest, "Peso: ", edges_weights[heaviest]
        print"Partial MST: ", mst
        print
    print"Final MST: ", mst
    print"Peso total da MST obtida: ", sum(mst.values())
    return mst
