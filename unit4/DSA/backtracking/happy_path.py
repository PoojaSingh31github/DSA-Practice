def countHappyPaths(H, W, grid):
    D = [(0, 1), (1, 0)] 
    visited = set()  
    count = 0 

    def backtrack(x, y):
        nonlocal count
        if x == H - 1 and y == W - 1:
            count += 1
            return
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                value = grid[nx][ny]  

                if value not in visited:
                    visited.add(value)  
                    backtrack(nx, ny)
                    visited.remove(value) 
    visited.add(grid[0][0])  
    backtrack(0, 0)  
    return count
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
print(countHappyPaths(H, W, grid))
