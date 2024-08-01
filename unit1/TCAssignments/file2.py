mat = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20

# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

# sx = 1

# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3  -->  6 9 --> 8 7 --> 4 --> 5

# [3, 3]   -->  n = 3   ,  m = 3
# (n * m)  -->  no. of elements

def spiral_traversal(n, m, mat):
  sx=0
  ex=(n-1)
  # ex , sx   -->   x-coordinates  (start , end)
  sy=0
  ey=(m-1)
  # sy , ey   -->   y-coordinates  (start , end)
  count = 0;
  while (sx<=ex) and (sy<=ey):
    # row-wise   sx   -->  [sy, ey]
    for i in range(sy, ey+1):
      print(mat[sx][i], end=" ")
    sx += 1
    if sx > ex:
      break;

    # column-wise   ey   -->  [sx, ex]
    for i in range(sx, ex+1):
      print(mat[i][ey], end=" ")
    ey -= 1
    if sy > ey:
      break;

    # row-wise   ex   -->  [ey, sy]
    for i in range(ey, sy-1, -1):
      print(mat[ex][i], end=" ")
    # sx += 1
    ex -= 1
    if sx > ex:
      break

    # column-wise   sy   -->  [ex, sx]
    for i in range(ex, sx-1, -1):
      print(mat[i][sy], end=" ")
    # ey -= 1
    sy += 1
    if sy > ey:
      break

spiral_traversal(3, 3, mat);
print()
spiral_traversal(4, 5, mat2);