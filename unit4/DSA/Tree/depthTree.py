# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def maxDepth(self,root):
      if not root:
        return  0
      else:
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
      
