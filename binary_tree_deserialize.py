from binary_tree import *

def deserialize_nf(nodes):
	if nodes == None: return None
	if len(nodes) == 0: return None

	root = Node(nodes[0])
	t = (len(nodes) - 1) / 2
	
	lnodes = nodes[1:t + 1]
	rnodes = nodes[t + 1:]
	
	read_tree_nf(root, lnodes, rnodes)
	return root

def deserialize_lr(nodes):
	if nodes == None: return None
	if len(nodes) == 0: return None

	t = (len(nodes) - 1) / 2
	root = Node(nodes[t])
	
	lnodes = nodes[0:t]
	rnodes = nodes[t + 1:]

	read_tree_lr(root, lnodes, rnodes)
	return root

def read_tree_lr(current, lnodes, rnodes):
	if current == None: return

	if len(rnodes) == 1:
		if (rnodes[0] != None):
			current.add_right(Node(rnodes[0]))
	else:
		t = (len(rnodes) - 1) / 2
		r = Node(rnodes[t])
		read_tree_lr(r, rnodes[0:t], rnodes[t + 1:])
		current.add_right(r)

	if len(lnodes) == 1:
		if (lnodes[0] != None):
			current.add_left(Node(lnodes[0]))
	else:
		t = (len(lnodes) - 1) / 2
		l = Node(lnodes[t])
		read_tree_lr(l, lnodes[0:t], lnodes[t+1:])
		current.add_left(l)

def read_tree_nf(current, lnodes, rnodes):
	if current == None: return

	if len(rnodes) == 1:
		if (rnodes[0] != None):
			current.add_right(Node(rnodes[0]))
	else:
		t = (len(rnodes) - 1) / 2
		r = Node(rnodes[0])
		read_tree_nf(r, rnodes[1:t + 1], rnodes[t + 1:])
		current.add_right(r)

	if len(lnodes) == 1:
		if (lnodes[0] != None):
			current.add_left(Node(lnodes[0]))
	else:
		t = (len(lnodes) - 1) / 2
		l = Node(lnodes[0])
		read_tree_nf(l, lnodes[1:t + 1], lnodes[t + 1:])
		current.add_left(l)

root = deserialize_nf(['A', 'B', 'D', 'E', 'C', 'F', None])
print root.to_string()

root = deserialize_lr(['D', 'B', 'E', 'A', 'F', 'C', None])
print root.to_string()
