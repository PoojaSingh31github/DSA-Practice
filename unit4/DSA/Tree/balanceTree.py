# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def isBalanced(self, root):
      def check(root):
        if not root:
          return 0
        LH = check(root.left)
        RH = check(root.right)
        if LH ==-1 or RH==-1:
          return -1
        if abs(LH-RH) > 1:
          return -1
        return max(LH,RH) + 1
        
      return check(root) != -1 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
        
