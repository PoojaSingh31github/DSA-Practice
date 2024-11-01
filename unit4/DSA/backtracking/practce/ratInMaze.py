def findPath(maze):
    def isSafe(x,y):
        return (0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and not visited[x][y])
    n=len(maze)
    if n==0:
        return []
    stack = [(0,0,[(0,0)])]  #x y path
    visited = [[0 for i in range(n)] for j in range(n)]
    moves = [(1,0),(0,1)]
    while stack:
        x, y, path = stack.pop()
        if (x, y)== (n-1,n-1):
            return path
        visited [x][y] = 1
        for dx , dy in moves:
            new_x , new_y = x+dx , y+dy
            if isSafe(new_x,new_y):
                stack.append((new_x,new_y, path+[(new_x,new_y)]))
    return []            

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
ans = findPath(maze)
print(ans)
