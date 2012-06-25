
def set_zero_intersection(m):
	if (len(m) == 0) or (len(m[0]) == 0):
		return m

	rc = len(m)
	cc = len(m[0])

	rows = [0] * rc

	columns = [0] * cc

	for r in range(rc):
		for c in range (cc):
			if m[r][c] == 0:
				rows[r] = 1
				columns[c] = 1
	
	for r in range(rc):
		for c in range (cc):
			if (rows[r] == 1) or (columns[c] == 1):
				m[r][c] = 0
	return m

def print_matrix(m):
	for row in m:
		print row

m = [[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 0, 1, 1]]

print 'Original:'
print_matrix(m)
print 'Zeroed:'
print_matrix(set_zero_intersection(m))
