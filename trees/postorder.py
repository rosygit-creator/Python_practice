#  left right root
# expected outcome: [4, 5, 2, 6, 3, 1]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(node, res):

    if node is None:
        return -1


    postorder(node.left, res)

    postorder(node.right, res)

    res.append(node.data)

    # find height of tree, and left nodes and right nodes count
    return res


# Example Usage:
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

res=[]
# Calculate the height of the tree
inorder_traversal = postorder(root, res)
print(f"The height of the tree is: {inorder_traversal}")