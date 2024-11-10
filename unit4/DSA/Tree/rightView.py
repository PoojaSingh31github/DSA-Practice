# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
  def rightUtil(self, root, level, maxLvl, res):
    if not root:
      return 
    
    if maxLvl[0] < level:
      res.append(root.val)
      maxLvl[0] = level
    
    self.rightUtil(root.right, level+1, maxLvl, res)
    self.rightUtil(root.left, level+1, maxLvl, res)
    
  def rightSideView(self, root) :
    res = []
    maxLvl = [-1]
    
    self.rightUtil(root, 0, maxLvl, res)
    
    return res