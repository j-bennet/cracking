from linked_list import Node, LinkedList

def remove_duplicates(ll):
	if (ll.head is None) or (ll.head.next is None):
		return ll

	h = {}
	
	n = ll.head
	while n is not None:
		if n.data in h:
			h[n.data] += 1
		else:
			h[n.data] = 1
		n = n.next

	p = ll.head
	n = ll.head.next
	
	while n is not None:
		if h[n.data] > 1:
			h[n.data] -= 1
			tmp = n.next
			p.next = tmp
			n = tmp
		else:
			p = n
			n = n.next

	return ll

def remove_duplicates_no_buffer(ll):
	
	if (ll.head is None) or (ll.head.next is None):
		return ll

	p = ll.head
	n = ll.head.next

	while n is not None:
		# check from head to current
		checker = ll.head
		while checker != n:
			if checker.data == n.data:
				tmp = n.next
				p.next = tmp
				n = tmp
				break
			checker = checker.next
		if checker == n:
			p = n
			n = n.next
	
	return ll

def test_remove_duplicates(ll, no_buffer):
	if no_buffer:
		print 'No buffer: ' + str(no_buffer) + ', ' + ll.to_string() + ' -> ' + remove_duplicates_no_buffer(ll).to_string()
	else:
		print 'No buffer: ' + str(no_buffer) + ', ' + ll.to_string() + ' -> ' + remove_duplicates(ll).to_string()

test_remove_duplicates(LinkedList([1, 1, 1, 2, 3, 4, 1, 1, 1]), False)
test_remove_duplicates(LinkedList([1]), False)
test_remove_duplicates(LinkedList([]), False)
test_remove_duplicates(LinkedList([1, 2, 3, 4]), False)
test_remove_duplicates(LinkedList([1, 1, 1]), False)

test_remove_duplicates(LinkedList([1, 1, 1, 2, 3, 4, 1, 1, 1]), True)
test_remove_duplicates(LinkedList([1]), True)
test_remove_duplicates(LinkedList([]), True)
test_remove_duplicates(LinkedList([1, 2, 3, 4]), True)
test_remove_duplicates(LinkedList([1, 1, 1]), True)
