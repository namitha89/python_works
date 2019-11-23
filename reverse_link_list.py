class Node:

    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self,val):
        self.data=val

    def getNextNode(self):
        return self.nextNode

    def setNextnode(self,val):
        self.nextNode = val

class LinkedList:

    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def addNode(self,data):
        newNode = Node(data,self.head)
        newNode.nextNode = self.head
        self.head = newNode

    def reverseList(self):
        prev = None
        curr = self.head
        next = curr.nextNode
        while curr:
            curr.nextNode = prev
            prev = curr
            curr = next
            if next:
                next = next.nextNode
        self.head = prev


    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nextNode


list1 = LinkedList()
list1.addNode(5)
list1.addNode(10)
list1.addNode(20)
list1.addNode(30)
list1.printList()
print('----------------')
list1.reverseList()
list1.printList()
