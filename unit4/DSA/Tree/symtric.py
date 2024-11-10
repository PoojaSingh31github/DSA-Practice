# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below
class Solution:
    def isSymmetric(self,root):
      
      def isMirror(t1, t2):
        
        if not t1 and not t2:
          return True
        if not t1 or not t2:
          return False
        
        return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

      if not root:
        return True
      
      return isMirror(root.left, root.right)
      
