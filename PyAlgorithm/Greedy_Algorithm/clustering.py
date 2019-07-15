'''
k-clustering max spacing algorithm:

Given k number of clusters, find the max spacing between those k clusters
'''

import random
import math

def generate_points(num_points):
	points = []
	while len(points) < num_points:
		curr_point = [random.randint(0, 1000), random.randint(0, 1000)]
		if curr_point not in points:
			points.append(curr_point)
	return points

def calcDistance(point1, point2):
	sum1 = math.pow(point1[0] - point2[0], 2)
	sum2 = math.pow(point1[1] - point2[1], 2)
	return math.sqrt(sum1 + sum2)

def find_group_with_smallest_spacing(curr_group, target_groups):
	result = []
	round_smallest = float("inf")
	for p1 in curr_group:
		for group in target_groups:
			for p2 in group:
				curr_distance = calcDistance(p1, p2)
				if curr_distance < round_smallest:
					round_smallest = curr_distance
					result = [group, round_smallest]
	return result

def find_k_max_spacing_clustering(points, k):
	group_container = [[point] for point in points]
	while len(group_container) != k:
		round_group_to_merge = None
		round_group_from_merge = None
		round_smallest = float("inf")
		index = 0
		while index < len(group_container):
			group = group_container[index]
			target_groups = [g for g in group_container if g is not group]
			round_result = find_group_with_smallest_spacing(group, target_groups)
			if round_result[1] < round_smallest:
				round_group_from_merge = group
				round_smallest = round_result[1]
				round_group_to_merge = round_result[0]
			index += 1
		round_group_from_merge += round_group_to_merge
		group_container.remove(round_group_to_merge)
	return group_container


if __name__ == '__main__':
	#points = [[1, 1], [1, 2], [1, 4], [2, 2], [1, 6], [1, 5], [2, 1], [2, 5], [7, 1], [7, 2], [8, 1], [8, 2]]
	points = generate_points(10)
	print find_k_max_spacing_clustering(points, 5)
