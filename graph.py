class Vertex:
	name = None
	data = None

	def __init__(self, name, data):
		self.name = name
		self.data = data

	def __eq__(self, other):
		if isinstance(other, Vertex):
			return self.name == other.name
		return False

	def __ne__(self, other):
		if isinstance(other, Vertex):
			return self.name != other.name
		return False
	
	def to_string(self):
		s = '(' + str(self.name) + ', ' + str(self.data) + ')'
		return s

class Edge:
	src = None
	dst = None
	weight = None

	def __init__(self, src, dst, weight = 1):
		self.src = src
		self.dst = dst
		self.weight = weight

	def __eq__(self, other):
		if isinstance(other, Edge):
			return (self.src == other.src) and (self.dst == other.dst)
		return False

	def __ne__(self, other):
		if isinstance(other, Edge):
			return (self.src != other.src) or (self.dst != other.dst)
		return False

class Graph:
	
	vertices = None
	edges = None

	def __init__(self):
		self.vertices = []
		self.edges = []

	def add_vertex(self, name, data):
		v = Vertex(name, data)
		if v not in self.vertices:
			self.vertices.append(v)
		return v

	def add_edge(self, src, dst, weight = 1):
		e = Edge(src, dst, weight)
		if e not in self.edges:
			self.edges.append(e)
		return e
	
	def get_adjacent(self, src):
		adj = []
		for e in self.edges:
			if (e.src.name == src.name):
				adj.append(e.dst)
		return adj

	def get_weight(self, src, dst):
		for e in self.edges:
			if e.src.name == src.name and e.dst.name == dst.name:
				return e.weight
		return None

	def to_string(self):
		s = '['
		for i in range(len(self.vertices)):
			v = self.vertices[i]
			s += "\n" + v.to_string() + ' => ['
			se = ''
			for a in self.get_adjacent(v):
				if len(se) > 0: se += ', '
				se += a.to_string()
			s += se
			s += ']'
			if i < (len(self.vertices) - 1):
				s += ', '
		s += "\n]"
		return s
