from sort import brutal_force

'''
Program created to count the number of inversions in a list (based on its sorted ascending order)

Eg: [1, 2, 3 , 5, 4] has one inversion since 5 is greater than 4
'''

def count_inversion(a):
    inversions = 0
    if len(a) == 2:
        returned = {}
        if a[0] > a[1]:
            inversions += 1
            b = brutal_force(a)
            returned['i'] = inversions
            returned['a'] = b
            return returned
    elif len(a) == 1:
        return {'a': [a[0]], 'i': inversions}
    mid = len(a) / 2
    left = count_inversion(a[0:mid])
    right = count_inversion(a[mid:])
    sorted_left = left['a']
    sorted_right = right['a']
    index = left_index = right_index = 0
    result_arr = []
    inversions += left['i'] + right['i']
    while index < len(a):
        if left_index < mid and right_index < len(sorted_right) and sorted_left[left_index] <= sorted_right[right_index]:
            result_arr.append(sorted_left[left_index])
            left_index += 1
        elif left_index < mid and right_index < len(sorted_right) and sorted_left[left_index] > sorted_right[right_index]:
            result_arr.append(sorted_right[right_index])
            inversions += mid - left_index
            right_index += 1
        if left_index == mid and right_index != len(sorted_right):
            result_arr += sorted_right[right_index:]
            break
        elif right_index == len(sorted_right) and left_index != mid:
            result_arr += sorted_left[left_index:]
            break
        index += 1
    final_return = {'a': result_arr, 'i': inversions}
    return final_return


def inversion(a):
    return count_inversion(a)['i']


if __name__ == '__main__':
    #f = open('data.txt')
    #lines = f.readlines()
    #lines = [int(line.strip()) for line in lines]
    #print inversion(lines)
    #f.close()
    a = [1]
    print count_inversion(a)['i']
