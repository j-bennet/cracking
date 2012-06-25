from binary_tree import *

bst = BinarySearchTree()

#n = Node(10)
#r = n.add_right(Node(12))
#rr = r.add_right(Node(13))
#rl = r.add_left(Node(11))

#l = n.add_left(Node(8))
#ll = l.add_left(Node(7))
#lr = l.add_right(Node(9))

bst.insert(Node(10))
bst.insert(Node(8))
bst.insert(Node(7))
bst.insert(Node(9))

print bst.to_string()