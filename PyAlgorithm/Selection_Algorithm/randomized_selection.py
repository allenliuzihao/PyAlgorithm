'''
Problem:
Given array A with n distinct element, and number k from 1 to n, find the kth largest element in the array as
fast as possible
'''

import random
import time


'''
Naive solution, sort the array and then output the kth largest element.
This runs in O(nlogn) averge case, O(N) in best case, as Python implements its
sorting using TimSort algorithm: http://en.wikipedia.org/wiki/Timsort
'''


def naive_selection(a, k):
    a.sort()
    return a[k - 1]

'''
Two functions below are utility for randomized selections
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


def choose_pivot(a, i, j):
    return random.randint(i, j)


'''
Very elegant randomized selection algorithm that runs in O(n) on average, O(n^2) in worst case

Below are general idea:
1.randomly find a pivot
2.partition the array using the pivot. Left: everthing less than pivot; Right: everything greater than pivot
3.check if the index of pivot less than k or not,
    a. if yes, it means k is after index of pivot, recurse on the right part of the array
    b. if no, recurse on the left part
    c. if k == index of pivot, then return the element at index of pivot
Analysis of the worst case running time:
    In the worst case, every time the pivot is the least element in the inspected array. Since partition takes linear
    time, and everytime we only opt out only 1 element in the array, the algorithm runs in O(N * N) time
Analysis of average case running time:
    Using linearality of expectation:
        First define phase i as phrase when array size (problem size) between (3 / 4)^(i + 1) * N and (3 / 4) ^ i * N.
        Define Xi as number recursive calls at each phrase. (So essentially if the problem size at each phrase is 75 percent
        greater than the size at the previous phrase, it will keep recursing at the current phrase). So the total run time is
        bounded by sum of Xi * c * n * (3 / 4) ^ i over each i in all phrases. (Take (3 / 4) ^ i since it is larger than
        (3 / 4) ^ (i + 1)). Now we need to figure out what is expected value of Xi at each phrase.
    Expected value of Xi at each phrase:
        Because we define each phrase as when array size is between (3 / 4)^(i + 1) * N and (3 / 4) ^ i * N, we know that if
        we achieve size less than 75 greater than 25, then we are ready for next phrase. Now, based on expectation analysis,
        the number of times we need to randomly choose the pivot to achieve 25 - 75 split is exactly 2. So we know Xi is constant
        at each step.
    Putting all together:
        If the put the results from above analysis all together, we get sum of 2 * c * n * (3 / 4) ^ i over each i in all phrases.
        Using geometric sequences rule, we get this is equal to 8cn, which means expected run time of this randomized selection 
        algorithm runs in O(n) time.

Experiments on run time analysis:
    I ran the algorithm with a randomly generated list and compared its performance against naive implmentation. Here is the result:
    case 1    
        naive:  0.00605487823486  seconds
        randomized:  0.00305008888245  seconds
    case 2
        naive:  0.00724411010742  seconds
        randomized:  0.0047869682312  seconds
    case 3
        naive:  0.00533294677734  seconds
        randomized:  0.00531911849976  seconds
    So most cases randomized algorithm runs faster than naive implementation

    However, when I use the list sorted in reversed order, the result is not as much satisfying

    case 1
        naive:  0.358333826065  seconds
        randomized:  4.12890195847  seconds
    case 2
        naive:  0.345193862915  seconds
        randomized:  9.67065191269  seconds
'''


def randomized_selection_helper(a, k, i, j):
    p_index = choose_pivot(a, i, j)
    p_new_index = partition(a, p_index, i, j)
    if p_new_index == k:
        return a[p_new_index]
    elif p_new_index > k:
        return randomized_selection_helper(a, k, i, p_new_index - 1)
    else:
        return randomized_selection_helper(a, k, p_new_index + 1, j)


def randomized_selection(a, k):
    return randomized_selection_helper(a, k - 1, 0, len(a) - 1)


if __name__ == '__main__':
    a = random.sample(range(100000), 10000)
    start_time = time.time()
    print naive_selection(a, 500)
    print "naive: ", time.time() - start_time, " seconds"
    start_time = time.time()
    print randomized_selection(a, 500)
    print "randomized: ", time.time() - start_time, " seconds"
