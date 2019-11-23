class Node:

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class LinkedList:

    def __init__(self, r= None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size +=1

    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self,d):
        this_node =d
        while this_node:
            if this_node.get_data == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        print("print the linkedlist...............")
        if self.root == None:
            return
        current = self.root
        print(current.to_string())
        while current.has_next():
            current = current.get_next()
            print(current.to_string())

    def reverseLinkedList(self):
        prev_node = None
        current = self.root
        while current != None:
            next_node = current.next_node
            current.next_node = prev_node
            prev_node = current
            current = next_node
        self.root = prev_node

    def  addTwoList(self,first,second):
        prev_node = None
        carry = 0
        temp = None

        while (first is not None and second is not None):

            fdata = 0 if first is None else first.get_data()
            sdata = 0 if second is None else second.get_data()

            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0

            sum = sum if sum < 10 else sum % 10

            # create a node to sum as data
            temp = Node(sum)

            if self.root is None:
                self.root = temp
            else:
                prev_node.next_node = temp

            prev_node = temp # set previous for next insertion

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next_node
            if second is not None:
                second = second.next_node

            if carry > 0:
                temp.next_node = Node(carry)








first = LinkedList()
first.add(5)
first.add(8)
first.add(10)
first.print_list()
# myList.remove(8)
# myList.find(5)
# myList.reverseLinkedList()
second = LinkedList()
second.add(6)
second.add(1)
second.add(9)


# second.print_list()

# result = LinkedList()
# result.addTwoList(first.root,second.root)
# print "\nResult list is ",
# result.print_list()





