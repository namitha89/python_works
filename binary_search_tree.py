class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key

    def find(self, d):
        # import pdb;pdb.set_trace()
        if self.val == d:
            return self
        elif d < self.val and self.left:
            return self.left.find(d)
        elif d > self.val and self.right:
            return self.right.find(d)
        return False

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inOrder(root):
    # import pdb;pdb.set_trace()
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)








r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
# inOrder(r)
res = r.find(30)
inOrder(res)