import unittest
import random
import sys

sys.path.append("../Selection_Algorithm")

from deterministic_selection import d_select, randomized_selection

class DeterministicSelectionTestCase(unittest.TestCase):
	def test_deterministic_selection_one_element(self):
		a = [1]
	 	k = 1
		self.assertEqual(d_select(a, k), 1, 'Error when try to select the only element from array!')

	def test_deterministic_selection_elements_sorted(self):
		a = [i for i in xrange(1, 1000)]
		k = 600
		self.assertEqual(d_select(a, k), 600, 'Error when try to select the kth element from sorted array!')


	def test_deterministic_selection_elements_reverse_sorted(self):
		a = [i for i in reversed(xrange(1, 1000))]
		k = 600
		self.assertEqual(d_select(a, k), 600, 'Error when try to select the kth element from reverse sorted array!')


	def test_deterministic_selection_random_elements(self):
		a = random.sample(range(100000), 100000)
		b = a[:]
		b.sort()
		k = random.randint(1, 100000)
		self.assertEqual(d_select(a, k), b[k - 1], 'Error when try to select the kth element from random array!')


class RandomSelectionTestCase(unittest.TestCase):
	def test_deterministic_selection_one_element(self):
		a = [1]
	 	k = 1
		self.assertEqual(randomized_selection(a, k), 1, 'Error when try to select the only element from array!')

	def test_deterministic_selection_elements_sorted(self):
		a = [i for i in xrange(1, 1000)]
		k = 600
		self.assertEqual(d_select(a, k), 600, 'Error when try to select the kth element from sorted array!')


	def test_deterministic_selection_elements_reverse_sorted(self):
		a = [i for i in reversed(xrange(1, 1000))]
		k = 600
		self.assertEqual(randomized_selection(a, k), 600, 'Error when try to select the kth element from reverse sorted array!')


	def test_deterministic_selection_random_elements(self):
		a = random.sample(range(100000), 100000)
		b = a[:]
		b.sort()
		k = random.randint(1, 100000)
		self.assertEqual(randomized_selection(a, k), b[k - 1], 'Error when try to select the kth element from random array!')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DeterministicSelectionTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(RandomSelectionTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite2)