def findDirection(n, mat, px, py, prev):
  curr_pos = [px, py]
  min_val = float('inf')

  if px - 1 >= 0 and mat[px - 1][py] > prev:
    curr_pos = [px - 1, py]
    min_val = mat[px - 1][py]

  if px + 1 < n and mat[px + 1][py] > prev and mat[px + 1][py] < min_val:
    curr_pos = [px + 1, py]
    min_val = mat[px + 1][py]

  if py + 1 < n and mat[px][py + 1] > prev and mat[px][py + 1] < min_val:
    curr_pos = [px, py + 1]
    min_val = mat[px][py + 1]

  if py - 1 >= 0 and mat[px][py - 1] > prev and mat[px][py - 1] < min_val:
    curr_pos = [px, py - 1]
    min_val = mat[px][py - 1]

  return curr_pos

def solve(n, mat, px, py, prev, path):
  if px < 0 or py < 0 or px >= n or py >= n or mat[px][py] <= prev:
    return "-1"
  
  path += str(mat[px][py]) + " "
  curr_pos = findDirection(n, mat, px, py, mat[px][py])

  if curr_pos[0] == px and curr_pos[1] == py:
    return path.strip()

  return solve(n, mat, curr_pos[0], curr_pos[1], mat[px][py], path)

n=4
px=1
py=2
mat = [
    [2, 3, 1, 4],
    [3, 5, 2, 8],
    [9, 7, 3, 1],
    [2, 4, 1, 1]
]
out = []
out.append(solve(n, mat, px - 1, py, mat[px][py], str(mat[px][py]) + " "))
out.append(solve(n, mat, px + 1, py, mat[px][py], str(mat[px][py]) + " "))
out.append(solve(n, mat, px, py + 1, mat[px][py], str(mat[px][py]) + " "))
out.append(solve(n, mat, px, py - 1, mat[px][py], str(mat[px][py]) + " "))

for path in out:
  print(path)