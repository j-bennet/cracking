from graph import *
from stack_queue import *

state_unvisited = 'unvisited'
state_visiting  = 'visiting'
state_visited   = 'visited'

def has_route_bfs(g, src, dst):
	if src == dst: return True
	
	state = {}
	for v in g.vertices:
		state[v.name] = state_unvisited

	q = Queue()
	state[src.name] = state_visiting
	q.enqueue(src)

	while not q.is_empty():
		v = q.dequeue()

		if v == dst: return True

		for a in g.get_adjacent(v):
			if state[a.name] == state_unvisited:
				if a == dst:
					return True
				else:
					state[a.name] = state_visiting
					q.enqueue(a)

		state[v.name] = state_visited

	return False

def has_route_dfs(g, src, dst):
	if src == dst: return True
	
	state = {}
	for v in g.vertices:
		state[v.name] = state_unvisited

	stack = Stack()
	state[src.name] = state_visiting
	stack.push(src)

	while not stack.is_empty():
		v = stack.pop()

		if v == dst: return True

		for a in g.get_adjacent(v):
			if state[a.name] == state_unvisited:
				if a == dst:
					return True
				else:
					state[a.name] = state_visiting
					stack.push(a)

		state[v.name] = state_visited

	return False

def test_has_route(g, src, dst):
	has_bfs = str(has_route_bfs(g, src, dst))
	has_dfs = str(has_route_dfs(g, src, dst))
	print 'Found route from ' + src.to_string() + ' to ' + dst.to_string() + ', BFS: ' + has_bfs + ', DFS: ' + has_dfs

g = Graph()
v1 = g.add_vertex('A', 1)
v2 = g.add_vertex('B', 2)
v3 = g.add_vertex('C', 3)
v4 = g.add_vertex('D', 4)
v5 = g.add_vertex('E', 5)
v6 = g.add_vertex('F', 6)
v7 = g.add_vertex('G', 7)
v8 = g.add_vertex('H', 8)

g.add_edge(v1, v2);
g.add_edge(v1, v3);
g.add_edge(v2, v4);
g.add_edge(v2, v5);
g.add_edge(v3, v6);
g.add_edge(v3, v7);
g.add_edge(v5, v8);

print g.to_string()

test_has_route(g, v1, v8)
test_has_route(g, v3, v8)
