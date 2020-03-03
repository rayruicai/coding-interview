# 18.5 in Elements of Programming Interviews in Python (Sep 15, 2016)
# design an algorithm that takes a reference to a vertex u, and creates
# a copy of the graph on the vertices reachable from u.

import unittest

# time complexity O(n+k)
# space complexity O(n+k)

def clone_graph(graph, u):
    if u not in graph:
        return None

    n = len(graph)
    edges = [graph[i] for i in graph]
    k = len([i for edge in edges if edge != [] for i in edge])

    # BFS
    graph_sub = {}
    graph_sub[u] = graph[u]
    vertices_reachable = [i for i in graph[u]]
    while vertices_reachable != []:
        v = vertices_reachable.pop(0)
        if v not in graph_sub:
            graph_sub[v] = graph[v]
            vertices_reachable += [i for i in graph[v] if i not in vertices_reachable]

    return graph_sub

class Test(unittest.TestCase):
    def test_clone_graph(self):
        graph = dict([(1, [2, 3, 4]), (2, [3]), (3, []), (4, [3]), (5, [2])])
        u = 1
        graph_sub = dict([(1, [2, 3, 4]), (2, [3]), (3, []), (4, [3])])
        self.assertEqual(clone_graph(graph, u), graph_sub);

if __name__ == "__main__":
    unittest.main()
