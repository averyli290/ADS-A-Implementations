from graph import *

# Other way to get cut nodes:
# start traversing from start node, run DFS, check if there are v - 1 nodes traversed not including the start node
# if not, then it is a cut node
# V * (V + E) = V * E time


'''
Algorithm

Criteira for cut node:
v is a cut node if at least one of the descendants and its subtree
have no back edges that connect to the ancestors of v.


Big assumption in recursion:
reach_data[v] stores the time of the highest reaching edge
or back edge from v or its descendants. This means that v
will be at maximum its parent's time value.

Let G be a graph, run a DFS on G.
Let v be the current node in DFS traversal at time t. We keep
track of the highest reaching (in the tree) aka earliest time
that any descendant of a node n is connected to via an edge in 
reach_data. In other words, we keep track of the lowest time of 
the highest reaching edge of any descendant of n in reach_edges[n].

For each neighbor w of v:
    if w has been visited:
        if w is not the parent of v then it must be a back edge.
        We update reach_data[v] = min(reach_data[v], time of w)
    if w has not been visited:
        Recurse on w

        if reach_data[w] >= t (current time) then there are no
        back edges reaching above v in w or descendants of w.
        Then, v is a cut node.


Proof of conjecture:

If v is a cut node then v has at least one descendant whose subtree with no
back edges to v's ancestors or v is a root with more than 1 child.

if v is a root and is a cut node, v must have more than 1 child because
otherwise if we removed the node, the graph would still be connected.

if v is a cut node and is not the root, if every subtree has a back edge 
to an ancestor of v, then removing v would have no effect on the connectedness
of the graph. This is because since every tree is connected, if every subtree
is connected to an ancestor of v, there will still remain a path from every 
vertex in the subtree to the vertex with a back edge, which then connects to
one of v's ancestors, connecting it to the rest of the graph.



If v is a root with more than 1 child then it is a cut node, and if v is
a vertex with at least one descendant whose subtree has no back edges to
v's ancestors then v is a cut node.

if v is a root with more than 1 child, we know that the subtrees are only
connected together by the root because there is only one path from one 
vertex to another in the tree. If we then remove the root then those paths
will be broken and the graph will be disconnected.

if v is a vertex with at least one descendant whose subtree has no back edges
to v's ancestors then the only path from that descendant to v's ancestors passes
through the edge that connects v and the descendant. If we remove v, then that path
no longer exists and the tree is disconnected.
'''




def cut_nodes(G, current_node=None, time=None, time_data=None, reach_data=None, result=None, root=None):
    # returns list of cut nodes in G (result)

    # visited: tracks if node has been visited
    # time: tracks time in DFS
    # time_data: {node: time when at node}
    # reach_data: tracks time of highest reaching (in tree) back edge in descendants of node
    # {node: time of highest back edge}
    # result: cut nodes

    if current_node is None:
        # return ([], [], []) for empty graph
        if len(G.get_vertices()) == 0:
            return ([], [], [])

        current_node = G.get_vertices()[0]
        root = current_node
        time = [0]  # This will be saved across all function calls
        time_data = {}
        reach_data = {}
        result = set()

        # Checking if root is cut node
        if len(G.get_neighbors(current_node)) > 1:
            result.add(current_node)


    # mark as in time_data
    time[0] += 1
    time_data[current_node] = time[0]  # adding current_node's time to time_data
    reach_data[current_node] = time[0]  # Setting inital value for reach_data[current_node]


    # traverse through neighbors
    neighbors = sorted(G.get_neighbors(current_node))
    for neighbor in neighbors:

        # this must be a child of current_node
        if neighbor not in time_data:
            # recursing to get reach_data for neighbor
            cut_nodes(G, neighbor, time, time_data, reach_data, result, root)

            # checking if cut node
            # have to use time_data[current_node] because time[0] changed after recursion
            if ((reach_data[neighbor] >= time_data[current_node])
                    and (current_node != root)):
                result.add(current_node)

            # updating current_node's reach data with neighbor's (by transitivity descendant's)
            reach_data[current_node] = min(reach_data[current_node], reach_data[neighbor])


        else:
            # Back edge/parent handling: (updating reach_data of current_node)
            # take min of cur and neighbor's time
            reach_data[current_node] = min(reach_data[current_node], time_data[neighbor])
    

    return (result, time_data, reach_data)
