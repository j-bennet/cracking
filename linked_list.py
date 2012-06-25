class Node:
	
	data = 0
	next = None

	def __init__(self, data):
		self.data = data

	def append(self, data):
		tailnode = Node(data)
		
		n = self
		while n.next is not None:
			n = n.next
		
		n.next = tailnode

class LinkedList:
	
	head = None

	def __init__(self):
		self.head = None
	
	def __init__(self, from_list):
		if from_list is None:
			self.head = None
			return

		for data in from_list:
			self.append(data)

	def append(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			self.head.append(data)
	
	def remove(self, data):
		if self.head is None:
			return None

		if self.head.data == data:
			self.head = self.head.next
		else:
			p = self.head
			n = self.head.next
			while n is not None:
				if n.data == data:
					p.next = n.next
					break
				else:
					p = n
					n = n.next

		return self.head
	
	def to_string(self):
		s = '['
		
		n = self.head

		while n is not None:
			s = s + str(n.data)
			if n.next is not None:
				s = s + ', '
			n = n.next

		s = s + ']'
		return s

	def output(self):
		import sys
		sys.stdout.write(self.to_string())
		print ''
