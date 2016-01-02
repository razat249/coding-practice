class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def geTFirst(self):
		print self.head.next.value


node = Element(1)
node2 = Element(2)
ll = LinkedList(node)
ll.append(node2)
ll.geTFirst()