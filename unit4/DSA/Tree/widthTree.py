# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def mirror(self,root):
      
      if not root:
        return None
        
      self.mirror(root.left)
      self.mirror(root.right)
      
      root.left, root.right = root.right, root.left
      
      return root
      
