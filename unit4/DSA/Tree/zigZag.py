# Definition of Binary Tree Node
# class Node:

#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

# Complete the function below and Return a list containing ZigZag Traversal of Nodes
def Solution(root):
  if not root:
    return []

  queue = [root]
  result = []
  LTR = True  

  while queue:
    size = len(queue)
    N = [] 
    for i in range(size):
      curr = queue.pop(0)
      if LTR:
        N.append(curr.data)
      else:
        N.insert(0, curr.data)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)

    result.extend(N)  
    LTR = not LTR  
  
  return result