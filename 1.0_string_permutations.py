def permute(word, d):
	if len(word) > 0:
		print word
	if d < len(word):
		word = list(word)
		for i in range (d, len(word)):
			word[d], word[i] = word[i], word[d]
			permute(''.join(word), d + 1)

permute('abc', 0)