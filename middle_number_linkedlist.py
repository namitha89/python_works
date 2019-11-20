# Find the middle of a given linked list in C and Java
#geekforgeeks

class Node:

    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n

    def has_next(self):
        if self.next_node is None:
            return False
        return True

class LinkedList:

    def __init__(self,r=None):
        self.head = r
        self.size = 0

    def display(self):
        print("Linked list displayed below:--------------")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node


    def addList(self,d):
        if self.head is None:
            self.head = Node(d)
            self.last_node  = self.head
        else:
            self.last_node.next_node = Node(d)
            self.last_node = self.last_node.next_node
        self.size += 1

    def findMiddleElement(self,index):
        # print(index)
        if index == 1:
            current = self.head
        i = 1
        temp = self.head
        while i <= index and temp is not None:
            temp = temp.next_node
            # print(temp)
            i += 1
        if temp is None:
            print("Linked list is empty")
        else:
            print(temp.data)

list_one = LinkedList()
list_one.addList(1)
list_one.addList(2)
list_one.addList(3)
list_one.addList(4)
list_one.addList(5)
list_one.addList(6)
# print(list_one.size)
middle_element = list_one.size /2
# print(middle_element)
# list_one.display()
list_one.findMiddleElement(middle_element)
