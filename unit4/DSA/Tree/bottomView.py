from collections import deque
# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below
class Solution:
    def bottomView(self, root) :
      
      if not root:
        return 
      
      bw={}
      q = deque([(root, 0, 0)])
      
      while q:
        
        node, hd, lvl = q.popleft()
        
        if hd not in bw or bw[hd][1] <= lvl:
          bw[hd] = (node.val, lvl)
        
        if node.left:
          q.append((node.left, hd-1, lvl+1))
        if node.right:
          q.append((node.right, hd+1, lvl+1))
        
      result = [bw[hd][0] for hd in sorted(bw.keys())]
      return result  
