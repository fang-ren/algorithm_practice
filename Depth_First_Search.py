"""
author: Fang Ren (SSRL)

3/13/2017
"""


"""
Erik Demaine's lecture notes

DFS solves problems like topological sort, maze puzzle

recursion problem

"""


source = 'a'
graph = {'a':['b','c'], 'b':['a','c', 'd'], 'c':['a', 'b', 'd'], 'd':['b','c', 'e'], 'e':['d']}
map = {source: None}

def DFS(source, graph):
    for neighbor in graph[source]:
        if neighbor not in map:
            map[neighbor] = source
            DFS(neighbor, graph)
    return map

DFS(source, graph)