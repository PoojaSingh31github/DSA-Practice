# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def isSameTree(self, a, b):
      if not a and not b:
        return True
      if not a or not b or a.val!=b.val:
        return False
      return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)  
        
        
        
        
