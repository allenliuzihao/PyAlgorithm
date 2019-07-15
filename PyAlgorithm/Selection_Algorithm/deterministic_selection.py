'''
Problem:
Given array A with n distinct element, and number k from 1 to n, find the kth largest element in the array as
fast as possible
'''

from randomized_selection import randomized_selection, naive_selection
import random
import time


'''
Partition around the median.
'''


def partition(a, median, i, j):
    #find the index of median
    p_index = -1
    for index1 in xrange(i, j):
        if a[index1] == median:
            p_index = index1
    #first swap pivot value with the first element in subarray
    a[i], a[p_index] = a[p_index], a[i]
    pivot_left_bound = i
    for index2 in xrange(i + 1, j + 1):
        if a[index2] < median:
            a[pivot_left_bound + 1], a[index2] = a[index2], a[pivot_left_bound + 1]
            pivot_left_bound += 1
    #put the pivot back to its position
    a[i], a[pivot_left_bound] = a[pivot_left_bound], a[i]
    return pivot_left_bound


'''
Naive implementation for selection
'''


def naive_selection(a, k, i, j):
    array = a[:]
    array.sort()
    return array[k]


'''
Extract array of groups of 5. Then return that group.

Eg. [1, 2 ,3, 4, 5, 5, 6, 7, 8] => [[1, 2, 3, 4, 5],[5, 6, 7, 8]]
'''


def extract_array_of_five(a, i, j):
    groups_of_five = []
    temp = []
    count = 0
    for index in xrange(i, j + 1):
        if count == 5:
            groups_of_five.append(temp)
            count = 0
            temp = []
        temp.append(a[index])
        count += 1
    if len(temp) != 0:
        groups_of_five.append(temp)
    return groups_of_five


'''
Find the median of median in the array of groups of 5
'''


def sort_find_median_groups_of_five(groups_of_five):
    medians = []
    for array in groups_of_five:
        array.sort()
        if len(array) == 5:
            medians.append(array[2])
        else:
            medians.append(array[len(array) / 2])
    return medians

'''
Deterministic solution for selection problem.
Idea:
    Divide the array into groups of 5. Sort each (O(n))
    Find the median of each group. Put them in array C
    Recursivly call select algorithm to find the median of
    these medians in C; Return p as pivot
    Anything else is the same as randomized selection
Analysis:
    Sorting at each recursive step is O(n), there are two recursion
    first one takes T(n / 5) (since we recursively call select on groups of
    5.). The second one takes T(7 / 10n) (the median of median garantee that
    the pivot is greater than at least 30 percent of elements and smaller than
    another 30 percent. We take the upper bound, it is 70 percent).
    Using the recursion tree, we discover that T(n) = T((9/10)n). Using geometric sequences,
    we get algorithm runs in linear time

Additional analysis:
    why pivot is smaller and greater than 30%?
    the median of median is greater than 3 / 5 of 50 percent of the elements in array and 
    smaller than 3 / 5 of 50 percent of elements in array. so it is 30%.
'''


def deterministic_selection(a, k, i, j):
    if j - i + 1 < 3:
        return naive_selection(a, k, i, j)
    else:
        groups_of_five = extract_array_of_five(a, i, j)
        medians = sort_find_median_groups_of_five(groups_of_five)
        median_of_medians = deterministic_selection(medians, len(medians) / 2 - 1, 0, len(medians) - 1)
        p_new_index = partition(a, median_of_medians, i, j)
        if p_new_index == k:
            return a[p_new_index]
        elif p_new_index > k:
            return deterministic_selection(a, k, i, p_new_index - 1)
        else:
            return deterministic_selection(a, k, p_new_index + 1, j)


'''
Comparison against Randomized selection:

case1:
    randomized:  0.0037579536438  seconds
    deterministic:  0.0484538078308  seconds
case2:
    randomized:  0.01118683815  seconds
    deterministic:  0.0411410331726  seconds
case3:
    randomized:  0.0114908218384  seconds
    deterministic:  0.0341820716858  seconds

In general, randomized algorithm is always faster than deterministic algorithm

Comparison against naive implementation:
case:
    deterministic:  0.476972818375  seconds
    naive_selection:  0.0580520629883  seconds

In general, deterministic approach also can't beat naive_selection approach. The
theory proves it to be linear time but in practical, the deterministic is not as good
'''


def d_select(a, k):
    return deterministic_selection(a, k - 1, 0, len(a) - 1)


if __name__ == '__main__':
    a = random.sample(range(100000), 100000)
    b = a[:]
    b.sort()
    k = random.randint(1, 100000)
    print d_select(a, k), " ", b[k - 1]
    '''
    a = random.sample(range(100000), 100000)
    len_a = len(a)
    start_time = time.time()
    print randomized_selection(a, 5000)
    print "randomized: ", time.time() - start_time, " seconds"
    start_time = time.time()
    print d_select(a, 5000)
    print "deterministic: ", time.time() - start_time, " seconds"
    start_time = time.time()
    print naive_selection(a, 4999, 0, len_a - 1)
    print "naive_selection: ", time.time() - start_time, " seconds"
    '''