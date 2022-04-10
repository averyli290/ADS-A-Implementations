from graph import *

# Problem 1
'''
3 DFS trees

o–o-o-o-o-o

o-o-o-o
     \
      o-o

o-o-o-o
   \
    o-o
'''


# Problem 2
'''
a)
The E's start_time is after B's and E's end_time is after B's

b)
The start/end_times of T_E are all before the stard/end_times of T_D

c)
E can be connected to B, A, and any other vertex in T_E.
For v in T_E, it can be connected by a back edge to any vertex
lying on the path connecting v and A.

'''

# Problem 3
def DFS_tree(G, start_node, visited=None, parent=None, tree=None):
	# Show DFS tree starting from start_node on graph G

	if tree is None:
		tree = []
	if visited is None:
		visited = {v: False for v in G.get_vertices()}

	# Add parent child connection to the list to return
	if parent is not None:
		tree.append((parent, start_node))

	# Mark as visited
	visited[start_node] = True

	# Traverse to next nodes
	for neighbor in sorted(G.get_neighbors(start_node)):
		if not visited[neighbor]:
			DFS_tree(G, neighbor, visited, start_node, tree)

	return tree


# Problem 4

'''
Algorithm:
Traverse through tree using regular DFS algorithm,
if there is a back edge, then there is is a cycle.

Proof:
Let v be the number of vertices in G. If there is a
back edge, then there are at least v edges in G,
therefore, there must be a cycle in G.
'''

def has_cycle(G, parent=None, current_node=None, visited=None):
	# Returns true if G has cycle, false otherwise
	# Solution: DFS the graph, if node has already been visited when looking
	# through neighbors and node isn't parent, there exists a cycle

	# Initial setup
	if current_node is None:
		current_node = G.get_vertices()[0]
	if visited is None:
		visited = {v: False for v in G.get_vertices()}

	# Mark as visited
	visited[current_node] = True

	# Tracking variable
	cycle_exists = False

	# Traverse to next nodes
	for neighbor in sorted(G.get_neighbors(current_node)):
		if not visited[neighbor]:
			# Updating cycle_exists
			cycle_exists = has_cycle(G, current_node, neighbor, visited) or cycle_exists
		elif neighbor != parent:
			# If neighbor has already been visited and is not parent, then there exists a cycle
			return True

	return cycle_exists
