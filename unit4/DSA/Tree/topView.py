# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below
class Solution:
    def util(self,root,hd,l,dic):
      if not root:
        return
      if hd not in dic or l<dic[hd][1]:
        dic[hd] = (root.val,l)
      self.util(root.left,hd-1,l+1,dic)  
      self.util(root.right,hd+1,l+1,dic)  
      
    def topView(self, root):
      dic = {}
      self.util(root, 0, 0, dic)
      sortedVal = sorted(dic.keys())
      res = [dic[hd][0] for hd in sortedVal]
      return res
      
      





