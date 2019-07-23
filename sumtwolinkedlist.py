# python program to add numbers represented by linkedlist

class Node:

	#constructor to intialize node object

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, element):
		node = Node(element)
		if self.head is None:
			self.head = node
		if self.tail is None:
			self.tail = node
		self.tail.next = node
		self.tail = node

	def insert(self,element,pos):
		node = Node(element)
		current = self.head
		# print(current)
		count = 0
		while True:
			if(count == pos):
				previousNode.next = node
				node.next = current
				break
			previousNode = current
			current = current.next
			count += 1


	def printLinkedList(self):
		current = self.head
		while (current is not None):
			print(current.data)
			current = current.next



ll = LinkedList() 
ll.add(1)
ll.add(3)
ll.add(4)
ll.add(5)

ll.insert(2, 1)
ll.printLinkedList()

# ll_2 = LinkedList() 
# ll_2.add(4)
# ll_2.add(6)
# ll_2.add(5)
# ll_2.printLinkedList()
		









