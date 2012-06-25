from linked_list import Node, LinkedList

def add_lists(l1, l2):

	if (l1 is None) or (l2 is None) or ((l1.head is None) and (l2.head is None)):
		return None
	
	ll = LinkedList([])
	
	h = 0
	n1 = l1.head
	n2 = l2.head

	if n1 is not None: h += n1.data
	if n2 is not None: h += n2.data

	digit = h % 10
	remember = (h - (h % 10)) / 10
	ll.append(digit)

	while (n1 is not None) or (n2 is not None):
		h = 0
		if n1 is not None: n1 = n1.next
		if n2 is not None: n2 = n2.next
		if n1 is not None: h += n1.data
		if n2 is not None: h += n2.data
		
		h += remember
		digit = h % 10
		remember = (h - (h % 10)) / 10
		
		if (n1 is not None) or (n2 is not None):
			ll.append(digit)
		else:
			if digit > 0:
				ll.append(digit)
			if remember > 0:
				ll.append(remember)

	return ll

print add_lists(LinkedList([1, 1, 1]), LinkedList([9, 9, 9])).to_string()
print add_lists(LinkedList([1]), LinkedList([9, 9, 9])).to_string()
print add_lists(LinkedList([1]), LinkedList([2, 2])).to_string()
