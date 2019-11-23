class Node:

    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getNextNode(self):
        return self.nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def setNextNode(self, val):
        self.nextNode = val

class LinkedList:

    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self,data):
        newNode = Node(data,self.head)
        newNode.nextNode = self.head
        self.head = newNode

    def removeNode(self,val):
        this_node =self.head
        prev_node = None
        while this_node:
            if this_node.getData() == val:
                if prev_node:
                    prev_node.nextNode = this_node.nextNode
                else:
                    self.head = this_node
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.nextNode

    def printData(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


mylist = LinkedList()
print("Inserting")
mylist.addNode(5)
mylist.addNode(10)
mylist.addNode(15)
mylist.printData()
print('after remove ----------------------')
mylist.removeNode(10)
mylist.printData()
