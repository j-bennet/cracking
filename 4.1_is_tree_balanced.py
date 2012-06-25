from binary_tree import *

def is_balanced(n):
	maxd = max_depth(n)
	mind = min_depth(n)
	print 'Max depth: ' + str(maxd)
	print 'Min depth: ' + str(mind)

	return ((maxd - mind) <= 1)

def max_depth(n):
	if n is None:
		return 0
	return 1 + max(max_depth(n.left), max_depth(n.right)) 

def min_depth(n):
	if n is None:
		return 0
	return 1 + min(min_depth(n.left), min_depth(n.right))

n = Node(10)
r = n.add_right(Node(12))
rr = r.add_right(Node(13))
rl = r.add_left(Node(11))

l = n.add_left(Node(8))
ll = l.add_left(Node(7))
lr = l.add_right(Node(9))

print 'Balanced: ' + str(is_balanced(n))
