from graph import *


def DFS_component(G, node, visited=None, traverse=None):
	# DFS traversal of a component in G

	if visited is None:
		# keeps track of which nodes have been visited
		visited = {v: False for v in G.get_vertices()}

	if traverse is None:
		traverse = []


	visited[node] = True  # mark node as visited
	traverse.append(node)  # add to traverse order

	# Traverse neighbors that are not visited yet
	sorted_neighbors = sorted(G.get_neighbors(node))  # Using alphabetical order
	for neighbor in sorted_neighbors:
		if not visited[neighbor]:
			DFS_component(G, neighbor, visited, traverse)

	return traverse


def DFS_full(G):
	# keeps track of which nodes have been visited
	visited = {v: False for v in G.get_vertices()}

	visited_order = []

	num_components = 0
	for node in visited:
		if not visited[node]:
			# traverse component if node not visited, pass in visited to update
			visited_order += DFS_component(G, node, visited)
			num_components += 1

	return (visited_order, num_components)


def DFS_component_with_times(G, node, visited=None, time=0, output=None):
	# DFS traversal of component with start and end times of visiting nodes recorded

	if visited is None:
		# keeps track of which nodes have been visited
		visited = {v: False for v in G.get_vertices()}

	if output is None:
		output = []


	visited[node] = True  # mark node as visited
	start_time = time  # record start time


	# Traverse neighbors that are not visited yet
	for neighbor in sorted(G.get_neighbors(node)):
		if not visited[neighbor]:
			DFS_component_with_times(G, neighbor, visited, time + 1, output)


	# calculating end_time (will be max of all times listed + 1)
	max_time = start_time  # max_time will have to be at least start_time (required for leaves in graph)

	for i in range(len(output)):
		# comparing to end times already listed (end_time always greater than start_time)
		max_time = max(output[i][2], max_time)

	end_time = max_time + 1  # get end_time value


	output.append((node, start_time, end_time))  # record times to output

	return output[::-1]  # reverse list to get correct traversal order
