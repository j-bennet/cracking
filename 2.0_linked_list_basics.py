from linked_list import Node, LinkedList

ll = LinkedList(range(1, 11))

to_remove = [2, 1, 8]

print 'Original:'
ll.output()


for i in to_remove:
	print 'Removed ' + str(i) + ':'
	ll.remove(i)
	ll.output()
