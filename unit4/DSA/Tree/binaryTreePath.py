# Definition of Binary Tree Node
# class Node:

#     def __init__(self, val):

#         self.left = None
#         self.right = None
#         self.val = val

# Complete the function below

class Solution:
    def treePaths(self,root):
      if not root:
        return []
        
      def DFS(root,curr):
        curr+=str(root.val)
        if not root.left and not root.right:
          path.append(curr)
        else:
          if root.left:
            DFS(root.left,curr+"->")
          if root.right:
            DFS(root.right,curr+"->")
      path=[]
      DFS(root,"")
      return path
        
        
        
        
        
      
