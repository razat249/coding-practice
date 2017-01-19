# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)

# while head != None:
# 	print head.val
# 	head = head.next
def reverseList(p):
	if (p.next == None):
		head = p
		# print head.val
		return head
	head = reverseList(p.next)
	p.next.next = p
	p.next = None
	return head


head = reverseList(p)
# print head
while head != None:
	print head.val
	head = head.next