from linked_list import Node, LinkedList

def find_before_last(ll, steps):
	if (ll is None) or (ll.head is None) or (steps < 0):
		return None

	i = 0
	fast = ll.head
	found = None
	while (i <= steps) and (fast is not None):
		if i == steps:
			found = fast
			break
		fast = fast.next
		i += 1
	
	if found is None:
		return None # list too short

	slow = ll.head
	
	while (fast != None) and (fast.next != None):
		slow = slow.next
		fast = fast.next

	return slow.data

def test_find_before_last(ll, n):
	found = find_before_last(ll, n)
	print ll.to_string() + ', ' + str(n) + ' -> ' + str(found)

for i in range(-1, 11, 1):
	test_find_before_last(LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), i)
