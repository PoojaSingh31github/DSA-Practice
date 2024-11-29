def largest_forest(matrix, n):
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  visited = [[False] * n for _ in range(n)]
  
  def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    size = 0
    while stack:
      cx, cy = stack.pop()
      size += 1
      # Explore neighbors
      for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == 'T':
          visited[nx][ny] = True
          stack.append((nx, ny))
    return size


  max_forest_size = 0
  for i in range(n):
    for j in range(n):
      if matrix[i][j] == 'T' and not visited[i][j]:
        forest_size = dfs(i, j)
        max_forest_size = max(max_forest_size, forest_size)
  
  return max_forest_size

n = 5
matrix = [
    ['T', 'T', 'T', 'W', 'W'],
    ['T', 'W', 'W', 'T', 'T'],
    ['T', 'W', 'W', 'T', 'T'],
    ['T', 'W', 'T', 'T', 'T'],
    ['W', 'W', 'T', 'T', 'T']
]

print(largest_forest(matrix, n))
