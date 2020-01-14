class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkidList:

    def __init__(self):
        self.head = None

    def create(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def mergeList(l1,l2):
    # import pdb;pdb.set_trace()
    newList = Node(0)
    curr = newList
    # print(curr.next)
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return newList.next

def printNewList(newl):
    while newl:
        print(newl.data)
        newl = newl.next




node1 = LinkidList()
node1.create(4)
node1.create(1)

# node1.printList()

node2 = LinkidList()
node2.create(2)
node2.create(1)

# node2.printList()

new = LinkidList()
# print(node2.head)
res = mergeList(node1.head,node2.head)
printNewList(res)








