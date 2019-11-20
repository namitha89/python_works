# https://leetcode.com/problems/merge-two-sorted-lists/
class Node:

    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data = d

    def to_string(self):
        return "Node Value: " +str(self.data)

    def has_next(self):
        if self.next_node is None:
            return False
        return True

class LinkedList:

    def __init__(self,r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size +=1

    def print_list(self):
        print("print the linkedlist...............")
        if self.root == None:
            return
        current = self.root
        print(current.to_string())
        while current.has_next():
            current = current.get_next()
            print(current.to_string())

    def merge_sorted_linkedlist(self, first, second):

        temp = None
        head = None
        # import pdb;pdb.set_trace()
        while (first is not None and second is not None):
             # 1-2-3   # 1-4-5  # 1-1
             if first.get_data() <= second.get_data():

                 if temp is None:
                     temp = Node(first.get_data())
                     head = temp
                 else:
                     temp.next_node = Node(first.get_data())
                     temp = temp.next_node
                 first = first.next_node
             else:
                if temp is None:
                    temp = Node(second.get_data())
                else:
                    temp.next_node = Node(second.get_data())
                    temp = temp.next_node
                second = second.next_node


        if first is None:
            temp.next_node = second
            return head
        if second is None:
            temp.next_node = first
            return head

first = LinkedList()
first.add(1)
first.add(2)
first.add(3)
first.print_list()

second = LinkedList()
second.add(1)
second.add(4)
second.add(5)
# second.print_list()

mergelist = LinkedList()
mergelist.merge_sorted_linkedlist(first.root,second.root)
mergelist.print_list()



