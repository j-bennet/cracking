class Node:
	data = None
	left = None
	right = None

	def __init__(self, data):
		self.data = data

	def add_left(self, n):
		if self.left == None:
			self.left = n
		else:
			self.left.add_left(n)
		return n

	def add_right(self, n):
		if self.right == None:
			self.right = n
		else:
			self.right.add_right(n)
		return n

	def to_string(self):
		s = '[' + str(self.data) + ' => [' 
		
		if self.left != None: s += str(self.left.data)
		else: s += 'None'

		s += ', '

		if self.right != None: s += str(self.right.data)
		else: s += 'None'
		
		s += "]]\n"

		if self.left != None: s += self.left.to_string()
		if self.right != None: s += self.right.to_string()

		return s

class BinarySearchTree:

	root = None

	def insert(self, node, parent = None):
		
		if self.root is None:
			self.root = node
			return self.root

		if parent is None: parent = self.root

		if node.data < parent.data:
			if parent.left is None:
				parent.left = node
				return parent.left
			else:
				return self.insert(node, parent.left)
		else:
			if parent.right is None:
				parent.right = node
				return parent.right
			else:
				return self.insert(node, parent.right)

	def to_string(self):
		if self.root is None:
			return '[]'
		return self.root.to_string()
