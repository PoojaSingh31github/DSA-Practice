def wordMatrix(n,m,board,word):

    def DFS(i,j,index):
        if index ==len(word):
            return True
        if i>=n or i<0 or j>=m or j<0 or board[i][j] !=word[index]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        for x,y in direction:
            if DFS(i+x , j+y,  index+1):
                return True

        board[i][j] = temp
        return False    


    direction = [
        [0,1],[0,-1],[1,0],[-1,0]   # east west  south nnoth
    ]
    for i in range(n):
        for j in range(m):
            if DFS(i,j,0):
                return True
    return False        


n,m = 3,4
board=[
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'N', 'E', 'E']
]
word="SEEN"
print(wordMatrix(n,m,board,word))
