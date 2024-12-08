mat = [
    ["jack", 158, 85, 112],
    ["john", 168, 74, 124],
    ["arti", 148, 65, 120],
    ["bhuvan", 182, 84, 124],
    ["navi", 182, 84, 124],
    ["vijay", 175, 88, 115],
    ["amit", 180, 89, 119],
    ["kevin", 182, 77, 120],
    ["rohit", 174, 85, 100],
    ["vivek", 184, 75, 111],
]

n=len(mat)
for i in range(n):
  for j in range(n-i-1):
    s1=mat[j]
    s2=mat[j+1]
    if  (s1[3] < s2[3]) or (s1[3] == s2[3] and s1[1] < s2[1]) or \
           (s1[3] == s2[3] and s1[1] == s2[1] and s1[2] > s2[2]) or \
           (s1[3] == s2[3] and s1[1] == s2[1] and s1[2] == s2[2] and s1[0] > s2[0]):
             mat[j], mat[j+1] = mat[j+1], mat[j]
for i in range(8):
  print(mat[i][0])
