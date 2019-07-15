'''
Given n items, each has value: value vi, size wi

capacity of knapsack: capacity W

output subset that maximize sum of values subject to capacity constraint
'''

'''
items = [[value, size, name], [value, size, name], ...]
'''
def solve_knapsack(items, capacity):
	solution = []
	# first initialize the cache
	for i in xrange(0, len(items) + 1):
		temp = []
		for j in xrange(0, capacity + 1):
			temp.append(0)
		solution.append(temp)
	# then the calculation
	for i in xrange(1, len(items) + 1):
		for j in xrange(1, capacity + 1):
			if j - items[i - 1][1] < 0:
				solution[i][j] = solution[i - 1][j]
			else:
				solution[i][j] = max(solution[i - 1][j], solution[i - 1][j - items[i - 1][1]] + items[i - 1][0])
	index_i = len(items)
	index_j = capacity
	selected = []
	while index_i >= 1 and index_j >= 1:
		if index_j - items[index_i - 1][1] >= 0 and solution[index_i - 1][index_j - items[index_i - 1][1]] + items[index_i - 1][0] > solution[index_i - 1][index_j]:
			selected.append(items[index_i - 1][2])
			index_j -= items[index_i - 1][1]
		index_i -= 1
	return {'max value': solution[len(items)][capacity], 'selected list': selected}

if __name__ == '__main__':
	print solve_knapsack([[5, 5, 'a'],[6, 4, 'b'],[12 ,1, 'c'], [20, 12, 'd']], 9)
