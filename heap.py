class Heap:
	q = []

	def parent(self, i):
		if i == 0:
			return None
		return (i + 1) / 2 - 1
	
	def young_child(self, i):
		return (i + 1) * 2 - 1
	
	def insert(self, n):
		self.q.append(n)
		self.bubble_up(len(self.q) - 1)
	
	def bubble_up(self, i):
		pi = self.parent(i)
		if pi is None:
			return

		if self.q[pi] > self.q[i]:
			self.q[pi], self.q[i] = self.q[i], self.q[pi]
			self.bubble_up(pi)
	
	def bubble_down(self, i):
		ci = self.young_child(i)
		min_ix = i
		for j in range(0, 2):
			if (ci + j) < len(self.q):
				if self.q[min_ix] > self.q[ci + j]:
					min_ix = ci + j
		
		if min_ix != i:
			self.q[i], self.q[min_ix] = self.q[min_ix], self.q[i]
			self.bubble_down(min_ix)
	
	def make_heap(self, nodes):
		self.q = []
		for n in nodes:
			self.insert(n)
	
	def extract_min(self):
		if len(self.q) == 0:
			return None
		n = None
		if len(self.q) > 1:
			n = self.q[0]
			self.q[0] = self.q.pop(len(self.q) - 1)
			self.bubble_down(0)
		else:
			n = self.q.pop()
		return n