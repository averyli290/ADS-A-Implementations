from bin_heap import BinaryHeapForEdges
from weighted_graph import *


def MST_Prim(G):
    # Prim's Algorithm

    # data to return
    solution_edges = []
    total_weight = 0

    # Setup
    edges_found = set()
    vertices_found = set()
    num_vertices = len(G.get_vertices())
    prio_q = BinaryHeapForEdges()

    min_edge = list(G.get_all_edges())[0]
    for edge in list(G.get_all_edges()):
        if edge.weight < min_edge.weight:
            min_edge = edge

    # adding min edge data
    vertices_found.add(list(min_edge.vertices)[0])
    vertices_found.add(list(min_edge.vertices)[1])
    edges_found.add(min_edge)

    # updating solution data to include min edge
    solution_edges.append(min_edge)
    total_weight += min_edge.weight

    # adding inital edges to heap from first vertices
    add_edges_to_heap(prio_q, G, list(min_edge.vertices)[0], edges_found)
    add_edges_to_heap(prio_q, G, list(min_edge.vertices)[1], edges_found)

    while len(vertices_found) < num_vertices:

        # Search for next good edge. edge good if only have one vertex in visited
        # Can check if both vertices in visited because one has to be
        good_edge = None
        while good_edge is None:

            # Popping min edge from heap and getting vertices
            temp_edge = prio_q.get_min()
            prio_q.delete_min()
            temp_vertices = list(temp_edge.vertices)

            if not ((temp_vertices[0] in vertices_found) 
                    and (temp_vertices[1] in vertices_found)):
                good_edge = temp_edge

        # Update found sets
        edges_found.add(good_edge)
        new_vertex = list(good_edge.vertices)[0]
        if new_vertex in vertices_found:
            new_vertex = list(good_edge.vertices)[1]
        vertices_found.add(new_vertex)

        # Update edge queue
        add_edges_to_heap(prio_q, G, new_vertex, edges_found)

        # Update solution + weight
        solution_edges.append(good_edge)
        total_weight += good_edge.weight

    return solution_edges, total_weight


def add_edges_to_heap(heap, G, vertex, edges_found):
    # Adds all edges connected to vertex to heap that haven't been found
    for edge in G.get_edges(vertex):
        #print(edge)
        if edge not in edges_found:
            heap.insert(edge)

            # Add edge to found edges for no repeat
            edges_found.add(edge)

if __name__=="__main__":
    data = [ ('A','B',1), ('B','C',2), ('D','E',3), ('E','F',5), ('G','H',3), ('H','I',2), ('A','D',1), ('B','E',1), ('C','F',3), ('D','G',1), ('E','H',2), ('F','I',4) ]
    G = WeightedGraph(data)
    output = MST_Prim(G)
    print(output)

