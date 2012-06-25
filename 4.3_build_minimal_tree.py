from binary_tree import *

def create_minimal_tree(a):
	return add_to_tree(a, 0, len(a) - 1)

def add_to_tree(a, l, r):
	if l > r: return None
	
	m = l + (r - l) / 2

	n = Node(a[m])
	n.left = add_to_tree(a, l, m - 1)
	n.right = add_to_tree(a, m + 1, r)

	return n

t = create_minimal_tree(range(0, 11))
print t.to_string()