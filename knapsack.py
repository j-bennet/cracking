def knapsack_cost(items, costs, max_count):
	maxcost = []
	
	total_items = 0
	
	for i in range(len(items)):
		total_items += items[i]

	for i in range(total_items + 1):
		maxcost.append(-1)
	
	maxcost[0] = 0

	for i in range(1, len(maxcost)):
		i_max_thing = -1
		max_thing_cost = -1
		for j in range(len(costs)):
			if items[j] > 0 and max_thing_cost < costs[j]:
				max_thing_cost = costs[j]
				i_max_thing = j
		if i_max_thing != -1:
			maxcost[i] = maxcost[i - 1] + max_thing_cost
			items[i_max_thing] -= 1
			print 'Took item at ' + str(costs[i_max_thing]) + ', items left:', items
	
	print 'Max set costs:', maxcost
	return maxcost[max_count]

items = [2,  3,  4,  1]
costs = [1., 5., 2., 10.]
max_count = 8

print 'Max at ' + str(max_count) + ' is ' + str(knapsack_cost(items, costs, max_count))