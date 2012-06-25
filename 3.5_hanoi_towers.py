from stack_queue import *

def hanoi_towers(s1, s2, s3):
	move_stack(s1.length, s1, s3, s2)

def move_stack(n, source, dest, other):
	if n > 1:
		move_stack(n - 1, source, other, dest)
	dest.push(source.pop())
	if n > 1:
		move_stack(n - 1, other, dest, source)

s1 = Stack()

for i in range(10, 0, -1):
	s1.push(i)

s2 = Stack()

s3 = Stack()

print 'Before:'
print s1.to_string()
print s2.to_string()
print s3.to_string()

hanoi_towers(s1, s2, s3)

print 'After:'
print s1.to_string()
print s2.to_string()
print s3.to_string()
