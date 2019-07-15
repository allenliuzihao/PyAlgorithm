'''
File contains randomized quick sort that runs in O(nlogn) on average
'''

import random


'''
Given an array and its boundary, (all inclusive), return a random number from array index i to j
'''


def choose_pivot(a, i, j):
    return random.randint(i, j)


'''
Given an array and the pivot, swap element in array based on pivot value. All value less than pivot is at left of pivot
Else, all value bigger than pivot is at right. Return the index of the pivot
'''


def partition(a, p_index, i, j):
    #first swap pivot value with the first element in subarray
    p = a[p_index]
    a[i], a[p_index] = a[p_index], a[i]
    pivot_left_bound = i
    for index in xrange(i + 1, j + 1):
        if a[index] < p:
            a[pivot_left_bound + 1], a[index] = a[index], a[pivot_left_bound + 1]
            pivot_left_bound += 1
    #put the pivot back to its position
    a[i], a[pivot_left_bound] = a[pivot_left_bound], a[i]
    return pivot_left_bound


'''
Helper for quick sort: sort a from i to j index inclusive
'''


def quick_sort_helper(a, i, j):
    if i == j or i > j:
        return
    else:
        p_index = choose_pivot(a, i, j)
        p_new_index = partition(a, p_index, i, j)
        quick_sort_helper(a, i, p_new_index - 1)
        quick_sort_helper(a, p_new_index + 1, j)


def quick_sort(a):
    quick_sort_helper(a, 0, len(a) - 1)


if __name__ == '__main__':
    a = [1, 0, 2, 1, 6, 4, 2, 3, 4, 10, 29, 10, 21]
    quick_sort(a)
    print a
