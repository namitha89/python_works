# https://leetcode.com/problems/merge-two-sorted-lists/
class Node:

    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self,n):
        self.next_node = n

    def has_next(self):
        if self.next_node is None:
            return False
        return True

class CirculatLinkedList:

    def __init__(self, r= None):
        self.head = r
        self.size = 0
        self.last_node = None

    def add(self,d):
        if self.head is None:
            self.head = Node(d)
            self.last_node = self.head
        else:
            self.last_node.next_node = Node(d)
            self.last_node = self.last_node.next_node

    def display(self):
        print("linked list displayed below:")
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.next_node

def print_values(head):
    while head:
        print(head.data)
        head = head.next_node
    print("----")

def merge_sorted_list(list1,list2):
    temp = None
    head = None
    # import pdb;pdb.set_trace()
    while(list1 is not None and list2 is not None):

            if list1.get_data() <= list2.get_data():

                if temp is None:
                    temp = Node(list1.get_data())
                    head = temp
                else:
                    temp.next_node = Node(list1.get_data())
                    temp = temp.next_node

                list1 = list1.next_node

            else:

                if temp is None:
                    temp = Node(list2.get_data())
                    head = temp
                else:
                    temp.next_node = Node(list2.get_data())
                    temp = temp.next_node

                list2 = list2.next_node
            # print_values(head)
    if list1 is None:
        temp.next_node = list2
        return head
    if list2 is None:
        temp.next_node = list1
        return head



list_one = LinkedList()
list_one.add(1)
list_one.add(2)
list_one.add(3)
# print(list_one.head.get_data())
# list_one.display()


list_two = LinkedList()
list_two.add(1)
list_two.add(4)
list_two.add(5)
# print(list_two.head.get_data())
# list_two.display()

merged_list = LinkedList()
list_one_head = list_one.head
list_two_head = list_two.head
res = merge_sorted_list(list_one_head,list_two_head)
print_values(res)







