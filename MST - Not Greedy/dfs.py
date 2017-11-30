#!/usr/bin/python


def dfs_cycle(mst, start):
    """Modified DFS to check for cycles"""
    colors = {node: "WHITE" for node in mst}
    colors[start] = "GRAY"
    stack = [(None, start)]  # store edge, but at this point we have not visited one
    while stack:
        (prev, node) = stack.pop()  # get stored edge
        for neighbor in mst[node]:
            if neighbor == prev:
                pass  # don't travel back along the same edge we came from
            elif colors[neighbor] == "GRAY":
                return True
            else:  # can't be anything else than WHITE...
                colors[neighbor] = "GRAY"
                stack.append((node, neighbor))  # push edge on stack
    return False
