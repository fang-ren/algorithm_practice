"""
author: Fang Ren (SSRL)

3/13/2017
"""

"""
Erik Demaine's lecture notes

BFS solves an exploring problem, for example a graph

graph object: G = (V, E)

V: set of vertices (nodes)
E: set of edges

edges can be:
    e = {v, w} unordered pair    undirected graph
    e = (v, w) ordered pair      directed graph

Undirected example:
V = {a,b,c,d}
E = {{a,b}, {a,c}, {b, c}, {b,d}, {c,d}}

hashtable representation: graph = {'a':['b','c'], 'b':['a','c', 'd'], 'c':['a', 'b', 'd']}

Directed example
V = {a,b,c}
E = {(a,c), (b,a), (b,c), (c,b)}

Application:
- web crawling
- social networking
- network broadcast
- garbage collection
- model checking
- solve puzzles
"""





graph = {'a':['b','c'], 'b':['a','c', 'd'], 'c':['a', 'b', 'd'], 'd':['b','c', 'e'], 'e':['d']}
source = 'a'

def explore(source, graph):
    """
    :param source:
    :param graph:
    :return: map
    # example: given a node "source", return a shortest path dict
    """
    # step = 0 initialization
    wavefront = [source]
    map = {source:0}
    step = 1
    while wavefront:
        next_nodes = []
        for current_node in wavefront:
            #print current_node, step, visited
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in map:
                    map[neighbor] = step
                    next_nodes.append(neighbor)
        wavefront = next_nodes
        step += 1
        #print map
    return map

map = explore(source, graph)

shortest_path = map['d']