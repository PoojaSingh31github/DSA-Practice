class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
            
    def _insert(self, curr, key):
        if key < curr.key:
            if curr.left is None:
                curr.left = Node(key)
            else:
                self._insert(curr.left, key)
        elif key > curr.key:
            if curr.right is None:
                curr.right = Node(key)
            else:
                self._insert(curr.right, key)
                
    def inorder_traversal(self, node=None):
        # If no node is provided, start from the root
        if node is None:
            node = self.root

        # Helper function to collect keys
        def _inorder(node):
            if node is None:
                return []
            return _inorder(node.left) + [node.key] + _inorder(node.right)

        return _inorder(node)

if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 20, 40, 70, 60, 80]
    for ele in elements:
        bst.insert(ele)

    print("Inorder Traversal:", bst.inorder_traversal())