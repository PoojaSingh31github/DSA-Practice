def detect_cycle(graph, n):
  visited = [False]*n
  stack = [False]*n
  
  def DFS(v):
    visited[v] =True
    stack[v] = True
    for i in graph[v]:
      if not visited[i]:
        if DFS(i):
          return True
      elif stack[i]:
        return True
    
    stack[v] = False
    return False
    
  for k in range(n):
    if not visited[k]:
      if DFS(k):
        return True
  return False
    

res=[]
for _ in range(int(input())):
  n,e = map(int,input().split())
  graph = [[] for j in range(n)]
  for i in range(e):
    x,y = map(int,input().split())
    graph[x].append(y)
    
  if detect_cycle(graph, n):
    res.append("Cycle")
  else:
    res.append("Not a cycle")
    
print("\n".join(res))
    