'''
#Definition of Binary Tree Node
#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.data = data
'''
#Complete the function below, and return the node of new bst

def merge(root1, root2):
  def inorder_traversal(root, result):
    if not root:
      return
    inorder_traversal(root.left, result)
    result.append(root.data)
    inorder_traversal(root.right, result)

  list1, list2 = [], []
  inorder_traversal(root1, list1)
  inorder_traversal(root2, list2)

  merged_list = []
  i, j = 0, 0
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i += 1
    else:
      merged_list.append(list2[j])
      j += 1

  while i < len(list1):
    merged_list.append(list1[i])
    i += 1
  while j < len(list2):
    merged_list.append(list2[j])
    j += 1
  
  return merged_list
