import unittest
import sys
import random

sys.path.append("../Data_Structure")

import heap

def isHeap(heap, option):
    index = 1
    while index <= heap.size():
        if 2 * index <= heap.size():
            if (option and heap.getArray()[index] > heap.getArray()[2 * index]) or (not option and heap.getArray()[index] < heap.getArray()[2 * index]):
                return False
        if 2 * index + 1 <= heap.size():
            if (option and heap.getArray()[index] > heap.getArray()[2 * index + 1]) or (not option and heap.getArray()[index] < heap.getArray()[2 * index + 1]):
                print heap.getArray()[index], " ", heap.getArray()[2 * index + 1]
                return False
        index += 1
    return True

class MinHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.heap = heap.Heap(True)

    def test_insert_extract_one_element_min_heap(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.size(), 1,
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after insertion!")
        extract = self.heap.extract()
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after extraction!")
        self.assertEqual(extract, 1,
                         'element extracted from heap is different from element inserted')

    def test_insert_extract_sorted_elements_min_heap(self):
        a = [i for i in xrange(1, 1000)]
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after extraction!")
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_insert_extract_reverse_sorted_elements_min_heap(self):
        a = [i for i in reversed(xrange(1, 1000))]
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after extraction!")
        extract.reverse()
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_insert_extract_random_elements_min_heap(self):
        a = random.sample(range(100000), 10000)
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after extraction!")
        a.sort()
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_remove_element_from_empty_min_heap(self):
        self.assertRaises(KeyError, self.heap.remove, (1))


    def test_remove_element_from_min_heap_with_one_element(self):
        self.heap.insert(1)
        removed = self.heap.remove(1)
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after removal!")
        self.assertEqual(removed, 1,
                         'elements removed are different from elements inserted!')
    
    def test_remove_min_element_from_min_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(1)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after removal!")
        self.assertEqual(removed, 1, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_max_element_from_min_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(999)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after removal!")
        self.assertEqual(removed, 999, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_middle_element_from_min_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(500)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, True), "not a heap after removal!")
        self.assertEqual(removed, 500, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_all_elements_from_min_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        for i in xrange(1, 1000):
            removed = self.heap.remove(i)
            self.assertEqual(self.heap.size(), 999 - i,
                         'incorrect heap size after removal of element: ' + str(i) + '!')
            self.assertTrue(isHeap(self.heap, True), "not a heap after removal of element: " + str(i) + '!')
            self.assertEqual(removed, i, "removed element is different from the target for removal. Element: " + str(i))


class MaxHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.heap = heap.Heap(False)

    def test_insert_extract_one_element_max_heap(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.size(), 1,
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after insertion!")
        extract = self.heap.extract()
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after extraction!")
        self.assertEqual(extract, 1,
                         'element extracted from heap is different from element inserted')

    def test_insert_extract_sorted_elements_max_heap(self):
        a = [i for i in xrange(1, 1000)]
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after extraction!")
        extract.sort()
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_insert_extract_reverse_sorted_elements_max_heap(self):
        a = [i for i in reversed(xrange(1, 1000))]
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after extraction!")
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_insert_extract_random_elements_max_heap(self):
        a = random.sample(range(100000), 10000)
        for i in a:
            self.heap.insert(i)
        self.assertEqual(self.heap.size(), len(a),
                         'incorrect heap size after insertion!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after insertion!")
        extract = []
        while not self.heap.isEmpty():
            extract.append(self.heap.extract())
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after extraction!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after extraction!")
        a.sort()
        extract.sort()
        self.assertEqual(extract, a,
                         'elements extracted are different from elements inserted!')

    def test_remove_element_from_empty_max_heap(self):
        self.assertRaises(KeyError, self.heap.remove, (1))


    def test_remove_element_from_max_heap_with_one_element(self):
        self.heap.insert(1)
        removed = self.heap.remove(1)
        self.assertEqual(self.heap.size(), 0,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after removal!")
        self.assertEqual(removed, 1,
                         'elements removed are different from elements inserted!')
    
    def test_remove_min_element_from_max_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(1)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after removal!")
        self.assertEqual(removed, 1, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_max_element_from_max_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(999)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after removal!")
        self.assertEqual(removed, 999, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_middle_element_from_max_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        removed = self.heap.remove(500)
        self.assertEqual(self.heap.size(), 998,
                         'incorrect heap size after removal!')
        self.assertTrue(isHeap(self.heap, False), "not a heap after removal!")
        self.assertEqual(removed, 500, "removed element is different from the target for removal")
        self.heap.emptyHeap()

    def test_remove_all_elements_from_max_heap(self):
        for i in xrange(1, 1000):
            self.heap.insert(i)
        for i in xrange(1, 1000):
            removed = self.heap.remove(i)
            self.assertEqual(self.heap.size(), 999 - i,
                         'incorrect heap size after removal of element: ' + str(i) + '!')
            self.assertTrue(isHeap(self.heap, False), "not a heap after removal of element: " + str(i) + '!')
            self.assertEqual(removed, i, "removed element is different from the target for removal. Element: " + str(i))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaxHeapTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(MinHeapTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
