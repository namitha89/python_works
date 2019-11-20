class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, data):
        # import pdb;pdb.set_trace()
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def searchBST(self, val):
        # import pdb;pdb.set_trace()
        if val < self.val:
            if self.left is None:
                return str(val)+" not found"
            return self.left.searchBST(val)
        elif val > self.val:
            if self.right is None:
                return str(val)+" not found"
            return self.right.searchBST(val)
        else:
            print(str(self.val) + " found")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()




root = Node(30)
root.insert(20)
root.insert(40)
root.insert(10)
root.insert(80)
root.PrintTree()
root.searchBST(20)



