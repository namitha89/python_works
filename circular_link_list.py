class Node:

    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n

    def has_next(self):
        if self.next_node is None:
            return False
        return True

class CircularLinikedList:

    def __init__(self,r=None):
        self.head = r

    def addCircularLinkedList(self,d):
        if not self.head:
            self.head = Node(d)
            self.head.next_node = self.head
        else:
            new_node = Node(d)
            curr = self.head
            while (curr.next_node != self.head):
                curr = curr.next_node
            curr.next_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def display(self):
        print("linked list displayed below:")
        current = self.head
        while current is not None:
            print "%d" % (current.data),
            current = current.next_node
            if current == self.head:
                break;




circular = CircularLinikedList()
circular.addCircularLinkedList(12)
circular.addCircularLinkedList(56)
circular.addCircularLinkedList(2)
circular.addCircularLinkedList(11)
circular.display()












