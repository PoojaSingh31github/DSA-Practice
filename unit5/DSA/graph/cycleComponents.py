from collections import defaultdict, deque

def count_cycles(n, m, edges):
  graph = defaultdict(list)
  for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
  
  visited = set()
  cycles = 0
  
  # Helper function to perform BFS/DFS
  def bfs(node):
      queue = deque([node])
      visited.add(node)
      vertices = 0
      edges = 0
      is_cycle = True
      
      while queue:
          curr = queue.popleft()
          vertices += 1
          degree = len(graph[curr])
          
          if degree != 2:
              is_cycle = False
          
          for neighbor in graph[curr]:
              edges += 1
              if neighbor not in visited:
                  visited.add(neighbor)
                  queue.append(neighbor)
      
      # Each edge is counted twice (u-v and v-u)
      edges //= 2
      return vertices, edges, is_cycle

  for node in range(1, n + 1):
      if node not in visited:
          vertices, edges, is_cycle = bfs(node)
          if is_cycle and vertices == edges and vertices >= 3:
              cycles += 1
  
  return cycles

n, m = 5 ,4

edges = []
matrix = [
    [1, 2],
    [3, 4],
    [5, 4],
    [3, 5]
]


print(count_cycles(n, m, edges))
