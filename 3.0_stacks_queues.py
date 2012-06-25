from stack_queue import *

s = Stack()
for i in range(11):
	s.push(i)
	print s.to_string()

while not s.is_empty():
	n = s.pop()
	print 'Got ' + str(n) + ', remaining: ' + s.to_string()

q = Queue()
for i in range(11):
	q.enqueue(i)
	print q.to_string()

while not q.is_empty():
	n = q.dequeue()
	print 'Got ' + str(n) + ', remaining: ' + q.to_string()
