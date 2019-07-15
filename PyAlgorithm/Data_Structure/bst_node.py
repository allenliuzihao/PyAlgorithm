'''
Code for binary tree node
'''

class TreeNode(object):
	def __init__(self, name):
		super(TreeNode, self).__init__()
		self.name = name
		self.value = 0.0
		self.left = None
		self.right = None
		self.leftEdgeVal = -1
		self.rightEdgeVal = -1

	def setLeftEdgeVal(self, value):
		self.leftEdgeVal = value

	def getLeftEdgeVal(self):
		return self.leftEdgeVal

	def setRightEdgeVal(self, value):
		self.rightEdgeVal = value

	def getRightEdgeVal(self):
		return self.rightEdgeVal
	
	def setValue(self, value):
		self.value = value

	def getValue(self):
		return self.value

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setLeft(self, node):
		self.left = node

	def getLeft(self):
		return self.left

	def setRight(self, node):
		self.right = node

	def getRight(self):
		return self.right

	def __str__(self):
		return "The name of this node: " + self.name + "; the value of this node: " + str(self.value)

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return other.__lt__(self)

	def __eq__(self, other):
		return self.value == other.value

	def __ne__(self, other):
		return not self.__eq__(other)
