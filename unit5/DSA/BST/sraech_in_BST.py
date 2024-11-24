# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def searchBST(self, root, val):
      if not root:
        return 
      
      if val==root.val:
        return root
        
      elif val < root.val:
        return self.searchBST(root.left, val)
      else:
        return self.searchBST(root.right, val)
        
      
      
      
        
      
      
