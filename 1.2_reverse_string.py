s = 'Reverse me'
ls = list(s)

l = len(ls)
print "Len: {0}".format(l)
for i in range (0, l / 2):
	e = l - i - 1
	ls[i], ls[e] = ls[e], ls[i]

for i in range (0, l):
	print "Letter {0}: {1}".format(i, ls[i])