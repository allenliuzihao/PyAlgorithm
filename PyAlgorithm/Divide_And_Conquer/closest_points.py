'''
File contains naive implementation of finding closest points in 2D plane (runs in O(n^2))
and Divide and Conquer implementation (runs in O(nlogn))

One interesting I discovered is that divide and conquer algorithm is no faster (some time)
even slower than the brutal force when the number of points is small < 1000. But as the number
of points get larger, the speed of the algorithm improves a lot.

To be more specific:
When number of points is 10000, the divide and conquer runs 127.121967077 seconds whereas
brutal force runs 149.292073011. It is just interesting to see the text book theory get proved
in real experiment
'''

import random
import math
import time

num_points = 10000

#
# Randomly generate 50 different points with 0 <= x <= 1000 and 0 <= y <= 1000
#


def generate_points():
    points = []
    while len(points) < num_points:
        curr_point = [random.randint(0, 1000), random.randint(0, 1000)]
        if curr_point not in points:
            points.append(curr_point)
    return points

#
# Given two points, a and b, calculate its euclidean distance
#


def calc_distance(a, b):
    x_difference = abs(a[0] - b[0])
    y_difference = abs(a[1] - b[1])
    return math.sqrt(math.pow(x_difference, 2) + math.pow(y_difference, 2))

#
# Extract the x or y value in a list of points
#


def extract(points, isX):
    if isX:
        result = [point[0] for point in points]
    else:
        result = [point[1] for point in points]
    return result

#
# Naive algorithm for finding the closest two points in a plane
#


def naive_find_closest_pair(points):
    closest_1 = []
    closest_2 = []
    closest_distance = 99999
    for point1 in points:
        for point2 in points:
            if point1 is not point2:
                distance = calc_distance(point1, point2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_1 = point1
                    closest_2 = point2
    return [closest_1, closest_2]


#
# Divide and Conquer for solving closest pair of points problem
#


def find_closest_pair(points):
    # sort points based on their x and y coordinate
    sort_on_x = points[:]
    sort_on_x.sort(cmp=lambda a, b: cmp(a[0], b[0]))
    sort_on_y = points[:]
    sort_on_y.sort(cmp=lambda a, b: cmp(a[1], b[1]))
    return find_closest_pair_helper(sort_on_x, sort_on_y, points)


def many_same_x_coord(points):
    same_x = 0
    all_x = [point[0] for point in points]
    for i in all_x:
        if points[0][0] != i:
            same_x += 1
    if same_x > len(points) / 2:
        return True
    else:
        return False

#
# helper for find_closest_pair
#


def find_closest_pair_helper(points_sort_x, points_sort_y, points):
    if len(points) <= 1:
        return None
    elif len(points) == 3 or len(points) == 2 or len(points) == 4 or len(points) == 5 or many_same_x_coord(points):
        return naive_find_closest_pair(points)
    mid = len(points_sort_x) / 2
    mid_point = points_sort_x[mid - 1]
    left_half = [point for point in points if point[0] <= mid_point[0]]
    right_half = [point for point in points if point[0] > mid_point[0]]
    left_points_sort_x = [point for point in points_sort_x if point[0] <= mid_point[0]]
    left_points_sort_y = [point for point in points_sort_y if point[0] <= mid_point[0]]
    right_points_sort_x = [point for point in points_sort_x if point[0] > mid_point[0]]
    right_points_sort_y = [point for point in points_sort_y if point[0] > mid_point[0]]
    left_closest = find_closest_pair_helper(left_points_sort_x, left_points_sort_y, left_half)
    right_closest = find_closest_pair_helper(right_points_sort_x, right_points_sort_y, right_half)
    if left_closest is not None:
        distance_left = calc_distance(left_closest[0], left_closest[1])
    if right_closest is not None:
        distance_right = calc_distance(right_closest[0], right_closest[1])
    if left_closest is not None and right_closest is not None:
        shortest_distance = distance_left if distance_left < distance_right else distance_right
        shortest_pair_so_far = left_closest if distance_left == shortest_distance else right_closest
    elif left_closest is not None or right_closest is not None:
        shortest_distance = distance_left if left_closest is not None else distance_right
        shortest_pair_so_far = left_closest if left_closest is not None else right_closest
    return count_split_pair(shortest_distance, mid_point, points_sort_y, shortest_pair_so_far)


#
# Helper for counting closest pair
#

def count_split_pair(shortest_distance_no_split, mid_point, points_sort_y, shortest_pair_so_far):
    shortest_distance = shortest_distance_no_split
    left_bound = mid_point[0] - shortest_distance
    right_bound = mid_point[0] + shortest_distance
    closest_1 = shortest_pair_so_far[0]
    closest_2 = shortest_pair_so_far[1]
    points_within_bound_sort_y = [point for point in points_sort_y if point[0] >= left_bound and point[0] <= right_bound]
    index = 0
    while index < len(points_within_bound_sort_y):
        index_temp = index + 1
        while index_temp < len(points_within_bound_sort_y) and index_temp - index != 7:
            temp_distance = calc_distance(points_within_bound_sort_y[index], points_within_bound_sort_y[index_temp])
            if temp_distance < shortest_distance:
                closest_1 = points_within_bound_sort_y[index]
                closest_2 = points_within_bound_sort_y[index_temp]
                shortest_distance = temp_distance
            index_temp += 1
        index += 1
    return [closest_1, closest_2]


if __name__ == '__main__':
    points = generate_points()
    #    try:
    start_time = time.time()
    naive_find_closest_pair(points)
    print "naive: ", time.time() - start_time, " seconds"
    start_time = time.time()
    find_closest_pair(points)
    print "divide_conquer ", time.time() - start_time, " seconds"