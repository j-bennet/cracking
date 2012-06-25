from binary_tree import *

def traverse_inorder(n):
	if n.left is not None:
		traverse_inorder(n.left)
	print str(n.data) + ' '
	if n.right is not None:
		traverse_inorder(n.right)

def traverse_preorder(n):
	print str(n.data) + ' '
	if n.left is not None:
		traverse_inorder(n.left)
	if n.right is not None:
		traverse_inorder(n.right)

def traverse_postorder(n):
	if n.left is not None:
		traverse_inorder(n.left)
	if n.right is not None:
		traverse_inorder(n.right)
	print str(n.data) + ' '

n = Node(10)
r = n.add_right(Node(12))
rr = r.add_right(Node(13))
rl = r.add_left(Node(11))

l = n.add_left(Node(8))
ll = l.add_left(Node(7))
lr = l.add_right(Node(9))

print n.to_string()

print 'In-order:'
traverse_inorder(n)

print 'Pre-order:'
traverse_preorder(n)

print 'Post-order:'
traverse_postorder(n)
