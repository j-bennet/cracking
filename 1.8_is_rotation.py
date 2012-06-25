
def is_substring(string, substring):
	
	result = string.find(substring)
	
	if result == -1:
		return False

	return True

tests = [
	['word', 'rdwo'],
	['abcdef', 'cdefab'],
	['abcdef', 'bcdef'],
]

for t in tests:
	print t[0] + ', ' + t[1] + ' : ' + str(is_substring(t[1] + t[1], t[0]))

