class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_height(node):

    if node is None:
        return -1


    left_height = tree_height(node.left)
    right_height = tree_height(node.right)

    # find height of tree, and left nodes and right nodes count
    return 1 + max(left_height, right_height)



# Example Usage:
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Calculate the height of the tree
height = tree_height(root)
print(f"The height of the tree is: {height}")