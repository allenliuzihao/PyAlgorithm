'''
code for binary tree
'''

import sys
from heap import Heap

sys.path.append("../Data_Structure")

from bst_node import TreeNode

class HuffmanBinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, words_stats):
		heap = Heap(True)
		for word in words_stats:
			node = TreeNode(word)
			node.setValue(words_stats[word])
			heap.insert(node)
		self.root = HuffmanBinaryTree.buildTree(words_stats, heap)

	@staticmethod
	def buildTree(words_stats, heap):
		if heap.size() == 1:
			root = TreeNode("Internal")
			root.setLeftEdgeVal(1)
			node = heap.extract()
			root.setLeft(node)
			return root
		elif heap.size() == 2:
			root = TreeNode("Internal")
			root.setLeftEdgeVal(1)
			root.setRightEdgeVal(0)
			node1 = heap.extract()
			root.setLeft(node1)
			node2 = heap.extract()
			root.setRight(node2)
			return root
		else:
			copy_stats = words_stats.copy()
			node1 = heap.extract()
			node2 = heap.extract()
			new_node = TreeNode(node1.getName() + "/" + node2.getName())
			new_node.setValue(node1.getValue() + node2.getValue())
			del copy_stats[node1.getName()]
			del copy_stats[node2.getName()]
			copy_stats[node1.getName() + "/" + node2.getName()] = node1.getValue() + node2.getValue()
			heap.insert(new_node)
			root = HuffmanBinaryTree.buildTree(copy_stats, heap)
			new_node.setName("Internal")
			new_node.setValue(0.0)
			new_node.setLeftEdgeVal(1)
			new_node.setRightEdgeVal(0)
			new_node.setLeft(node1)
			new_node.setRight(node2)
			return root

	def decode(self, string):
		result = ''
		curr_node = self.root
		for i in xrange(0, len(string)):
			curr_bit = int(string[i])
			if curr_node.getLeftEdgeVal() == -1 and curr_node.getRightEdgeVal() == -1:
				result += curr_node.getName()
				if curr_node.getName() == "Internal":
					result = "string not decodable"
					break
				curr_node = self.root
			if curr_bit == curr_node.getLeftEdgeVal():
				curr_node = curr_node.getLeft()
			elif curr_bit == curr_node.getRightEdgeVal():
				curr_node = curr_node.getRight()
		if curr_node.getName() != "Internal":
			result += curr_node.getName()
		else:
			result = "string not decodable"
		return result

	def printTree(self):
		HuffmanBinaryTree.printTreeHelper(self.root)

	def getEncoding(self):
		encoding = {}
		HuffmanBinaryTree.getEncodingHelper(self.root, encoding, '')
		return encoding

	@staticmethod
	def printTreeHelper(node):
		if node is not None:
			print "node name: " + node.getName() + " node value: " + str(node.getValue())
		if node.getLeft() is not None:
			print "left edge value: " + str(node.getLeftEdgeVal())
			HuffmanBinaryTree.printTreeHelper(node.getLeft())
		if node.getRight() is not None:
			print "right edge value: " + str(node.getRightEdgeVal())
			HuffmanBinaryTree.printTreeHelper(node.getRight())

	@staticmethod
	def getEncodingHelper(node, encoding, curr_string):
		if node.getLeft() is None and node.getRight() is None:
			encoding[node.getName()] = curr_string
		if node.getLeft() is not None:
			HuffmanBinaryTree.getEncodingHelper(node.getLeft(), encoding, curr_string + str(node.getLeftEdgeVal()))
		if node.getRight() is not None:
			HuffmanBinaryTree.getEncodingHelper(node.getRight(), encoding, curr_string + str(node.getRightEdgeVal()))
