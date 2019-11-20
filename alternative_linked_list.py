# https://leetcode.com/problems/merge-two-sorted-lists/
class Node:

    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n

    def has_next(self):
        if self.next_node is None:
            return False
        return True

class LinkedList:

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

    def merge_sorted_list(self, list2):
        temp = None
        p_curr = self.head
        q_curr = list2
        while (p_curr is not None and q_curr is not None):
            p_next = p_curr.next_node
            q_next = q_curr.next_node

            q_curr.next_node = p_next
            p_curr.next_node = q_curr

            p_curr = p_next
            q_curr = q_next

        list2 = q_curr







    def display(self):
        print("linked list displayed below:")
        current = self.head
        # print(current.data)
        while current is not None:
            print(current.data)
            current = current.next_node


def print_values(head):
    while head:
        print(head.data)
        head = head.next_node
    print("----")

list_one = LinkedList()
list_one.add(1)
list_one.add(2)
list_one.add(3)

list_two = LinkedList()
list_two.add(1)
list_two.add(4)
list_two.add(5)

#merge two lists
list_two_head = list_two.head
list_one.merge_sorted_list(list_two_head)
list_one.display()








