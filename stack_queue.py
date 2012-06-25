class Node:
	next = None
	data = 0

	def __init__(self, data):
		self.data = data
	
	def to_string(self):
		s = '['
		n = self
		while n is not None:
			s += str(n.data)
			n = n.next
			if n is not None: s += ', '
		s += ']'
		return s

class Stack:
	
	top = None
	length = 0

	def push(self, data):
		t = Node(data)
		t.next = self.top
		self.top = t
		self.length += 1

	def pop(self):
		if self.top is not None:
			data = self.top.data
			self.top = self.top.next
			self.length -= 1
			return data
		return None

	def to_string(self):
		if self.top is None:
			return '[]'
		return self.top.to_string()
	
	def is_empty(self):
		return self.top is None

class Queue:
	first = None
	last = None
	length = 0

	def enqueue(self, data):
		n = Node(data)
		if self.first is None:
			self.first = self.last = n
		else:
			if self.length == 1:
				self.first.next = n
			else:
				self.last.next = n
			self.last = n
		self.length += 1

	def dequeue(self):
		if self.first is not None:
			data = self.first.data
			self.first = self.first.next
			self.length -= 1
			if self.first is None: self.last = None
			return data
		return None

	def debug(self, message = None):
		if (message): print message
		if self.first is None:
			print 'First: None'
		else:
			print 'First: ' + str(self.first.data.name)
		if self.last is None:
			print 'Last: None'
		else:
			print 'Last: ' + str(self.last.data.name)
	
	def to_string(self):
		if self.first is None:
			return '[]'
		return self.first.to_string()
	
	def is_empty(self):
		return self.first is None
