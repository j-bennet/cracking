from linked_list import Node, LinkedList

def find_loop(ll):

	if (ll is None) or (ll.head is None):
		return None # no loop
	
	fast = ll.head
	slow = ll.head

	loop = None
	
	while (fast is not None) and (slow is not None):
		
		if (slow.next is None) or (fast.next is None) or (fast.next.next is None):
			return None # no loop

		slow = slow.next
		fast = fast.next.next
		
		if fast == slow:
			fast = ll.head
			
			while fast != slow:
				fast = fast.next
				slow = slow.next
			
			return slow

	return None

def make_loop(rng, data):
	ll = LinkedList(rng)
	x = None
	y = None
	n = ll.head
	while True:
		if n.data == data:
			x = n
		if n.next == None:
			y = n
			break
		n = n.next
	y.next = x
	return ll

for i in range(1, 9):
	l = find_loop(make_loop([1, 2, 3, 4, 5, 6, 7, 8], i))
	print str(i) + ': loop in ' + str(l.data)
