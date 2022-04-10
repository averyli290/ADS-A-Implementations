# My apologies for PEP8-non-compliance
import random


class WeightedEdge:
    # Attributes:
    # vertices: a set of the two vertex names
    # weight
    def __init__(self, node_1, node_2, weight):
        self.vertices = set([node_1, node_2])
        self.weight = weight
    def __repr__(self):
        return str((self.vertices, self.weight))


class WeightedGraph:
    # adjacencies is a list of triples: (v_1, v_2, weight)
    def __init__(self, adjacencies = []):
        # self.edges is a dictionary from vertices to a set
        # of WeightedEdge objects.
        self.edges = {}
        for triple in adjacencies:
            self.add_edge(triple)

    def __str__(self):
        return(str(self.edges))

    def add_edge(self, triple):
        (node_1, node_2, weight) = triple
        self.add_vertex(node_1)
        self.add_vertex(node_2)
        edge = WeightedEdge(node_1, node_2, weight)
        self.edges[node_1].add(edge)
        self.edges[node_2].add(edge)

    # Add an isolated vertex.
    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = set()

    # Returns a set of vertices.
    def get_vertices(self):
        return(set(self.edges.keys()))

    # Returns a set of WeightedObjects.
    def get_edges(self, node):
        return self.edges[node]

    # Returns the set of all WeightedEdge objects.
    def get_all_edges(self):
        output = set()
        for node in self.get_vertices():
            output = output.union((self.get_edges(node)))
        return output

    def is_empty(self):
        return (self.get_vertices==[])


if __name__=="__main__":
    data = [ ('A','B',1), ('B','C',2), ('D','E',3), ('E','F',5), ('G','H',3), ('H','I',2), ('A','D',1), ('B','E',1), ('C','F',3), ('D','G',1), ('E','H',2), ('F','I',4) ]
    G = WeightedGraph(data)
    print(G)
