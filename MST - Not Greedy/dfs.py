#!/usr/bin/python


def dfs_cycle(mst, start):
    edges = []
    colors = {node: "WHITE" for node in mst}
    colors[start] = "GRAY"
    stack = [(None, start)]
    while stack:
        (prev, node) = stack.pop()
        for neighbor in mst[node]:
            if neighbor == prev:
                pass
            elif colors[neighbor] == "GRAY":

                return True
            else:
                colors[neighbor] = "GRAY"
                stack.append((node, neighbor))
    return False
