import sys
import random
import unittest

sys.path.append("../Divide_And_Conquer")

import closest_points
import count_inversion
import integer_multiplication
import quick_sort
import sort


class MergeSortTestCase(unittest.TestCase):
    def setUp(self):
        self.merge_sort = sort.merge_sort

    def test_merge_sort_only_one_element(self):
        a = [1]
        sorted_result = self.merge_sort(a)
        self.assertEqual(sorted_result, a,
                         'the sorted version of array is different from original version of array')
    
    def test_merge_sort_with_elements_increasing_order(self):
        a = [i for i in xrange(0, 10000)]
        sorted_result = self.merge_sort(a)
        self.assertEqual(sorted_result, a,
                         'the sorted version of array has error in its ordering of elements')
    
    def test_merge_sort_with_elements_decreasing_order(self):
        a = [i for i in reversed(xrange(0, 10000))]
        sorted_result = self.merge_sort(a)
        a.sort()
        self.assertEqual(sorted_result, a,
                         'the sorted version of array has error in its ordering of elements')
    
    def test_merge_sort_with_random_elements(self):
        a = random.sample(range(100000), 10000)
        sorted_result = self.merge_sort(a)
        a.sort()
        self.assertEqual(sorted_result, a,
                         'the sorted version of array has error in its ordering of elements')


class QuickSortTestCase(unittest.TestCase):
    def setUp(self):
        self.qsort = quick_sort.quick_sort
    
    def test_quick_sort_with_only_one_element(self):
        a = [1]
        b = a[:]
        self.qsort(b)
        self.assertEqual(b, a,
                         'the sorted version of array is different from original version of array')
    
    def test_quick_sort_with_elements_increasing_order(self):
        a = [i for i in xrange(0, 10000)]
        b = a[:]
        self.qsort(b)
        self.assertEqual(b, a,
                         'the sorted version of array has error in its sorting9')

    def test_quick_sort_with_elements_decreasing_order(self):
        a = [i for i in reversed(xrange(0, 10000))]
        b = a[:]
        self.qsort(b)
        a.sort()
        self.assertEqual(b, a,
                         'the sorted version of array has error in its sorting')

    def test_quick_sort_with_random_elements(self):
        a = random.sample(range(100000), 10000)
        b = a[:]
        self.qsort(b)
        a.sort()
        self.assertEqual(b, a,
                         'the sorted version of array has error in its sorting')


class IntegerMultiplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.multiply = integer_multiplication.integer_multiply

    def test_case_one_digit(self):
        self.assertEqual(self.multiply(2, 2), 4,
                         '2 * 2 case failed')
        self.assertEqual(self.multiply(4, 8), 32,
                         '4 * 8 case failed')

    def test_case_two_digits(self):
        self.assertEqual(self.multiply(10, 18), 180,
                         '10 * 18 case failed')
        self.assertEqual(self.multiply(52, 80), 52 * 80,
                         '52 * 80 case failed')
    
    def test_case_three_digits(self):
        self.assertEqual(self.multiply(1222, 4568), 1222 * 4568,
                         '1222 * 4568 case failed: ' + str( self.multiply(1222, 4568)))
        self.assertEqual(self.multiply(1424, 9398), 1424 * 9398,
                         '1424 * 9398 case failed')

    def test_case_six_digits(self):
        self.assertEqual(self.multiply(122854, 468128), 122854 * 468128,
                         '122854 * 468128 case failed')
        self.assertEqual(self.multiply(544112, 998232), 544112 * 998232,
                         '544112 * 998232 case failed')

    def test_all_multiplication_within_1000(self):
        for i in xrange(0, 999):
           for j in xrange(0, 999):
                self.assertEqual(self.multiply(i, j), i * j,
                         'test all possible multiplication case failed')

class CountInversionTestCase(unittest.TestCase):
    def setUp(self):
        self.inversion = count_inversion.count_inversion

    def test_count_inversion_one_element(self):
        a = [1]
        inversions = self.inversion(a)['i']
        self.assertEqual(inversions, 0,
                         'error when counting inversions in array of size 1: ')
    
    def test_count_inversion_elements_increasing_order(self):
        a = [i for i in xrange(1, 1000)]
        inversions = self.inversion(a)['i']
        self.assertEqual(inversions, 0,
                         'error when counting inversions in sorted array')

    def test_count_inversion_elements_decreasing_order(self):
        a = [i for i in reversed(xrange(1, 1000))]
        inversions = self.inversion(a)['i']
        self.assertEqual(inversions, 498501, "error when counting inversions in sorted array")

    def test_count_inversion_elements_random_order(self):
        a = random.sample(range(100000), 10000)
        real_inversions = 0
        for index_1 in xrange(0, 10000):
            for index_2 in xrange(index_1 + 1, 10000):
                if a[index_1] > a[index_2]:
                    real_inversions += 1
        inversions = self.inversion(a)['i']
        self.assertEqual(inversions, real_inversions,
                         'error when counting inversions in array with random elements')



if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(MergeSortTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(QuickSortTestCase)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(IntegerMultiplicationTestCase)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(CountInversionTestCase)
    alltests = unittest.TestSuite([suite1, suite2, suite3, suite4])
    unittest.TextTestRunner(verbosity=2).run(alltests)