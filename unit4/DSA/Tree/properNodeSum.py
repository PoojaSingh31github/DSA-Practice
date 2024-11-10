"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
"""

def sumProperNode(root):
  if not root:
    return 0
  s=0
  q=[root]
  
  while q:
    CN = q.pop(0)
    if CN.left and CN.right:
      s+=CN.val
      
    if CN.left:
      q.append(CN.left)
    if CN.right:
      q.append(CN.right)
  return s    
    
    
    
    
  
  
  pass
