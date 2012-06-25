
def is_anagram(s1, s2):

	if (len(s1) != len(s2)):
		return False

	h1 = {}
	h2 = {}

	for i in range(len(s1)):
		if s1[i] in h1:
			h1[s1[i]] += 1
		else:
			h1[s1[i]] = 0

	for i in range(len(s2)):
		if s2[i] in h2:
			h2[s2[i]] += 1
		else:
			h2[s2[i]] = 0

	for c in h1.keys():
		if (c in h2) and (h2[c] == h1[c]):
			h2.pop(c)
		else:
			return False

	for c in h2.keys():
		if (c not in h1) or (h1[c] != h2[c]):
			return False

	return True

print is_anagram('xamarin', 'marinax')
print is_anagram('aaa', 'aab')
print is_anagram('aaa', '')
print is_anagram('aabb', 'abab')

