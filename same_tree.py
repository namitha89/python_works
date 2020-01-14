class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def identicalTrees(r1,r2):
    if r1 is None and r2 is None:
        return True
    if (r1 and r2) and (r1.val == r2.val):
        return identicalTrees(r1.left,r2.left) and identicalTrees(r1.right,r2.right)
    else:
        return False



root1 = Node(1)
root1.left = Node(2)
root1.right= Node(3)

root2 = Node(1)
root2.left= Node(2)
root2.right= Node(3)

if identicalTrees(root1, root2):
    print "Both trees are identical"
else:
    print "Trees are not identical"


