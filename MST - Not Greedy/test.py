#!/usr/bin/python

cycles = []

def kappa(meme):
    global graph
    global cycles
    global p_edges
    p_edges = []
    graph = meme
    for edge in graph:
        for node in edge:
            findNewCycles([node])
    #for cy in cycles:
     #   path = [str(node) for node in cy]
      #  s = ",".join(path)
       # print(s)
    return p_edges

def findNewCycles(path):
    start_node = path[0]
    next_node= None
    sub = []
    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
        if not visited(next_node, path):
                # neighbor node not on path yet
                sub = [next_node]
                sub.extend(path)
                # explore extended path
                findNewCycles(sub)
        elif len(path) > 2 and next_node == path[-1]:
                # cycle found
                p = rotate_to_smallest(path)
                inv = invert(p)
                if isNew(p) and isNew(inv):
                    for x in range(0, len(p)-1):
                        if p[x] < p[x+1]:
                            p_edges.append((p[x], p[x+1]))
                        else:
                            p_edges.append((p[x + 1], p[x]))
                    if p[0] < p[x+1]:
                        p_edges.append((p[0], p[x+1]))
                    else:
                        p_edges.append((p[x + 1]), p[0])
                    cycles.append(p)

def invert(path):
    return rotate_to_smallest(path[::-1])

#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def isNew(path):
    return not path in cycles

def visited(node, path):
    return node in path



