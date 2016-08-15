class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def search(self, find_val):
		