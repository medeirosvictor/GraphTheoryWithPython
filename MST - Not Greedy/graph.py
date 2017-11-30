#!/usr/bin/python


class Graph:
    def __init__(self, adj_list):
        self.nodes = [x for x in adj_list]
        self.edges = []
        self.graph = adj_list
        for node in adj_list:
            for connected in adj_list[node]:
                self.edges.append((node, connected[0], connected[1]))

    def getEdgeWeightDict(self):
        dict = {}
        for edge in self.edges:
            dict[(edge[0], edge[1])] = edge[2]
        return dict
