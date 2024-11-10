# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def leftSideView(self, root) :
      if not root:
        return []
      left = []  
      q=[root]
      while q:
        size = len(q)
        for i in range(size):
          CN = q.pop(0)
          if i==0:
            left.append(CN.val)
          
          if CN.left:
            q.append(CN.left)
          if CN.right:
            q.append(CN.right)
      return left      
            
          
        
      
      
