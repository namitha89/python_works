x = [2,3,4,5,6,8,10]

class  Node():
    def __init__(self, v, l, r):
        self.v = v
        self.l = l
        self.r = r


def create_tree(i):
    if i >= (len(x)):
        return None

    l_i = (2 * i) + 1
    r_i = l_i + 1

    left = create_tree(l_i)
    right = create_tree(r_i)
    node = Node(x[i], left, right)
    return node

def print_tree(tree, position="root"):

    if tree is None:
        return

    print(position + "-" + str(tree.v))
    print_tree(tree.l, "left")
    print_tree(tree.r, "right")


def bst(node):

    if not (node.l and node.r):
        return

    bst(node.l)
    bst(node.r)

    if node.l and (node.l.v > node.v):
        node.v, node.l.v = node.l.v, node.v

    if node.r and (node.r.v < node.v):
        node.v, node.r.v = node.r.v, node.v



tree = create_tree(0)
print_tree(tree)

print("--after--" * 10)
for i in range(len(x)):
        bst(tree)
print_tree(tree)

