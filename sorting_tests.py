from heap import *

def heap_sort(a):
	h = Heap()
	h.make_heap(a)
	for i in range(len(a)):
		a[i] = h.extract_min()
	return a

def selection_sort(a):
	ix_min = 0
	for i in range(len(a)):
		ix_min = i
		for j in range(i + 1, len(a)):
			if a[j] < a[ix_min]:
				ix_min = j
		if ix_min != i:
			a[ix_min], a[i] = a[i], a[ix_min]
		
	return a

def insertion_sort(a):
	for i in range(1, len(a)):
		j = i
		while (j > 0) and (a[j] < a[j - 1]):
			a[j], a[j - 1] = a[j - 1], a[j]
			j -= 1

	return a

def quick_sort(a):
	if len(a) <= 1: return a

	m = (len(a) - 1) / 2
	l = []
	r = []

	for i in range(len(a)):
		if i != m:
			if a[i] <= a[m]:
				l.append(a[i])
			else:
				r.append(a[i])

	l = quick_sort(l)
	r = quick_sort(r)

	l.append(a[m])
	l.extend(r)

	return l

def quick_sort_in_place(a):
	quick_sort_in_place_r(a, 0, len(a) - 1)
	return a

def quick_sort_in_place_r(a, l, r):
	if l < r:
		pi = l + (r - l) / 2;
		pi = quick_sort_partition(a, l, r, pi)
		quick_sort_in_place_r(a, l, pi - 1)
		quick_sort_in_place_r(a, pi + 1, r)

def quick_sort_partition(a, l, r, m):
	pivot = a[m]
	a[m], a[r] = a[r], a[m]
	ix = l

	for i in range(l, r):
		if a[i] < pivot:
			a[i], a[ix] = a[ix], a[i]
			ix += 1
	
	a[ix], a[r] = a[r], a[ix]
	return ix

def merge_sort(a):
	if len(a) <= 1: return a
	
	m = (len(a) - 1) / 2
	l = merge_sort(a[:m + 1])
	r = merge_sort(a[m + 1:])
	a = merge(l, r)
	return a

def merge(l, r):
	t = []
	i = 0
	j = 0
	while i < len(l) or j < len(r):
		if i < len(l) and j < len(r):
			if l[i] < r[j]:
				t.append(l[i])
				i += 1
			else:
				t.append(r[j])
				j += 1
		else:
			if i < len(l):
				t.append(l[i])
				i += 1
			else:
				t.append(r[j])

				j += 1
	return t

print 'Selection:'
print selection_sort([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])

print 'Insertion:'
print insertion_sort([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])

print 'Merge:'
print merge_sort([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])

print 'Quick:'
print quick_sort([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])

print 'Quick in-place:'
print quick_sort_in_place([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])

print 'Heap:'
print heap_sort([12, 11, 10, 2, 9, 1, 8, 5, 7, 15, 4, 3, 13, 14])