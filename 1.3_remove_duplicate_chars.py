
def remove_duplicates(s):
	l = len(s)
	
	if (l < 2):
		return s

	s = list(s)
	i_dest = 0
	i_check = 1

	while ((i_dest < l) and (i_check < l)):
		if (s[i_dest] == s[i_check]):
			i_check += 1
		else:
			i_dest += 1
			s[i_dest] = s[i_check]
			i_check += 1

	s = s[:i_dest+1]
	s = "".join(s)
	return s

print remove_duplicates('aaaa')
print remove_duplicates('abcd')
print remove_duplicates('aabccc')
print remove_duplicates('aaabbbccc')