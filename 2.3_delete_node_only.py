from linked_list import Node, LinkedList

def delete_node(n):
	if (n is None) or (n.next is None):
		return # can't do this
	
	n.data = n.next.data
	n.next = n.next.next

def find_node(from_node, data):
	if (data is None) or (from_node is None):
		return None
	
	n = from_node
	
	while n != None:
		if n.data == data:
			return n
		else:
			n = n.next
	
	return None

def test_delete_node(ll, data):
	out = ll.to_string()
	node = find_node(ll.head, data)
	out += ', delete ' + str(node.data)
	delete_node(node)
	out += ' -> ' + ll.to_string()
	print out	

for i in range(1, 6):
	test_delete_node(LinkedList([1, 2, 3, 4, 5]), i)
