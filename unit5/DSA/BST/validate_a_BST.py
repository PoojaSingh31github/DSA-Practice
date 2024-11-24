# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def isBST(self,root):
      while root:
        l=root.left
        r=root.right
        if l.val > root.val or r.val < root.val:
          return False
        return True  
        
      
      
      
      
      
      
      
      
      
      
