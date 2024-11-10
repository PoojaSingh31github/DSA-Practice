# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
  def mergeTrees(self, t1, t2):
    if not t1:
      return t2
    if not t2:
      return t1
      
    ans=Node(t1.val + t2.val)
    ans.left = self.mergeTrees(t1.left, t2.left)
    ans.right = self.mergeTrees(t1.right, t2.right)
    
    return ans
    
        
        
        
        
      
        
