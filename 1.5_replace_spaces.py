
def replace_spaces(s):
	cnt = 0
	
	for c in s:
		if c == ' ':
			cnt += 1
	
	if cnt == 0:
		return s
	
	r = list(s)
	r.extend(' ' * cnt * 2)
	
	l = len(s)
	new_len = l + cnt * 2

	for i in range(l - 1, 0, -1):
		if r[i] == ' ':
			r[new_len - 1] = '0'
			r[new_len - 2] = '2'
			r[new_len - 3] = '%'
			new_len -= 3
		else:
			r[new_len - 1] = r[i]
			new_len -= 1

	return "".join(r)

tests = ['test #1', 'this is even more spaces', 'what?']

for t in tests:
	print t + ' -> ' + replace_spaces(t)