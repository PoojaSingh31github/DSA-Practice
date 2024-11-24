class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert(self.root, key)
            
        
    def _insert(self, curr,key):
        if key < curr.key:
            if curr.left is None:
                curr.left = Node(key)
            else:
                self._insert(curr.left, key)
        elif key > curr.key:
            if curr.right is None:
                curr.right = Node(key)
            else:
                self._insert(curr.right,key)
                
    def inorder_traversal(self,node=None):
        
        
        
        
        
        return 7
        
if __name__ == "__main__":
    bst = BinarySearchTree()
    element = [50,30,20,40,70,60,80]
    for ele in element:
        bst.insert(ele)
    
    print(bst.inorder_traversal())    
                
        
                                                
           
        