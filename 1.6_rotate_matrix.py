m = []
l = 4
start = 0

for row in range(l):
	m.append(range(start, start + l, 1))
	start += l

print "Original:"
for row in m:
	print row	

def rotate_matrix(m):
	n = []
	
	for r in range(len(m)):
		n.append([0] * len(m))
	
	for r in range(len(m)):
		for c in range(len(m)):
			n[c][(len(m)-r-1)] = m[r][c]
	
	return n

def rotate_matrix_inplace(m):
	side_len = len(m)
	shift = 0

	while (side_len > 1):
		block_len = len(m[shift])-2*shift
		
		# save top row
		top = m[shift][shift:shift+block_len]
		
		# move left to top
		for r in range(shift, shift + block_len):
			m[shift][len(m)-r-1] = m[r][shift]
		
		# move bottom to left
		for c in range(shift, shift + block_len):
			m[c][shift] = m[len(m)-shift-1][c]
		
		# move right to bottom
		for c in range(shift, shift + block_len):
			m[len(m)-shift-1][c] = m[len(m)-c-1][len(m)-shift-1]
		
		# move top to right
		i = 0
		for r in range(shift, shift + block_len):
			m[r][len(m)-shift-1] = top[i]
			i += 1

		side_len /= 2
		shift += 1	
	
	return m

n = rotate_matrix(m)

print "Rotated:"
for row in n:
	print row	

n = rotate_matrix_inplace(m)

print "Rotated in place:"
for row in n:
	print row	
