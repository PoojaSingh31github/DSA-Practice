# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below
class Solution:
    def levelOrder(self, root):
      res=[]
      if not root:
        return res
 
      q=[root]
      while q:
        l=[]
        n=len(q)
        for i in range(n):
          CN = q.pop(0)
          l.append(CN.val)
          
          if CN.left:
            q.append(CN.left)
          if CN.right:
            q.append(CN.right)
        res.append(l)    
          
      return res  
        
        
        
        
      
