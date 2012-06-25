from graph import *
import sys

state_unvisited = 'unvisited'
state_visiting  = 'visiting'
state_visited   = 'visited'

def dijkstra(g, src, dst):
	if src == dst: return 0
	
	dist = {}
	prev = {}
	unvisited = []
	for v in g.vertices:
		dist[v.name] = sys.maxint
		prev[v.name] = None
		unvisited.append(v)

	dist[src.name] = 0
	
	while len(unvisited) > 0:
		n = extract_cheapest(unvisited, dist)
		for child in g.get_adjacent(n):
			w = g.get_weight(n, child)
			if dist[n.name] + w < dist[child.name]:
				dist[child.name] = dist[n.name] + w
				prev[child.name] = n.name

	p = dst.name
	path = []
	while True:
		path.append(p)
		if p == src.name:
			break
		p = prev[p]

	return dist[dst.name], path

def extract_cheapest(unvisited, dist):
	best_dist = None
	best_ix = 0
	for i in range(len(unvisited)):
		if best_dist == None or dist[unvisited[i].name] < best_dist:
			best_dist = dist[unvisited[i].name]
			best_ix = i

	best = unvisited.pop(best_ix)
	return best

def test_dijkstra(g, src, dst):
	print 'Shortest route from ' + src.to_string() + ' to ' + dst.to_string() + ': ' + str(dijkstra(g, src, dst))

g = Graph()
v = []
for i in range(11):
	v.append(g.add_vertex('V' + str(i), i))

g.add_edge(v[1], v[2]);
g.add_edge(v[1], v[3]);
g.add_edge(v[2], v[4]);
g.add_edge(v[2], v[5]);
g.add_edge(v[3], v[6]);
g.add_edge(v[3], v[7]);
g.add_edge(v[5], v[8]);

print g.to_string()

test_dijkstra(g, v[1], v[8])
