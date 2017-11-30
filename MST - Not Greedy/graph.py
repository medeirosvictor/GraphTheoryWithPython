#!/usr/bin/python

class Graph:
    def __init__(self, adj_list):
        self.nodes = [x for x in adj_list]
        self.edges = []
        for node in adj_list:
            for connected in adj_list[node]:
                self.edges.append((node, connected))

    def __len__(self):
        return len([x for x in self])