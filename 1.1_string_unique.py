
def is_unique_chars(s):
	chars = {}
	for i in range(len(s)):
		if (s[i] in chars):
			return False
		else:
			chars[s[i]] = 1
	return True

def is_unique_chars_optimized(s):
	counter = 0

	for i in range(len(s)):
		char_ix = ord(s[i]) - ord('a')
		if (counter & (1 << char_ix) > 0):
			return False
		else:
			counter |= (1 << char_ix)
	return True

strings = ['amiunique', 'abcd', '']

for s in strings:
	print "Unique: '" + s + "': " + str(is_unique_chars(s)) + ", " + str(is_unique_chars_optimized(s))