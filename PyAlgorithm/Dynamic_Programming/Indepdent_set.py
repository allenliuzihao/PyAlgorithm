'''
Given a path graph with non-negative weights on its vertices, get the independent set that has maximum weights
'''

'''
Input: 
	vertices: list of vertices connected in that order
'''
def solve_independent_set(vertices):
	solution = [0, vertices[1][1]]
	for i in xrange(2, len(vertices)):
		solution.append(max(solution[i - 1], solution[i - 2] + vertices[i][1]))
	solution_vertices = []
	index = len(solution) - 1
	while index >= 1:
		if solution[index - 1] >= solution[index - 2] + vertices[index][1]:
			index -= 1
		else:
			solution_vertices.append(vertices[index][0])
			index -= 2
	return [solution[-1], solution_vertices]

if __name__ == '__main__':
	print solve_independent_set([None, ['a', 1], ['b', 1], ['c', 1], ['d', 2]])
