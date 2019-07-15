'''
follwing contains brutal force sort and merge
sort for an array of numbers in python

File created by Allen Liu
'''


def brutal_force(a):
    b = a[:]
    for i in xrange(len(b)):
        for j in xrange(i + 1, len(b)):
            if b[j] < b[i]:
                b[i], b[j] = b[j], b[i]
    return b


def merge_sort(a):
    if len(a) < 3:
        return brutal_force(a)
    mid = len(a) / 2
    left = a[0:mid]
    right = a[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    result_arr = []
    index = left_index = right_index = 0
    while index < len(a):
        if left_index < mid and right_index < len(sorted_right) and sorted_left[left_index] <= sorted_right[right_index]:
            result_arr.append(sorted_left[left_index])
            left_index += 1
        elif left_index < mid and right_index < len(sorted_right) and sorted_left[left_index] > sorted_right[right_index]:
            result_arr.append(sorted_right[right_index])
            right_index += 1
        if left_index == mid and right_index != len(sorted_right):
            result_arr += sorted_right[right_index:]
            break
        elif right_index == len(sorted_right) and left_index != mid:
            result_arr += sorted_left[left_index:]
            break
        index += 1
    return result_arr


if __name__ == '__main__':
    print merge_sort(a)
