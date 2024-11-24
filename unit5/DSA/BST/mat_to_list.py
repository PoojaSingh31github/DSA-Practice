for _ in range(int(input())):
    n = int(input())  # number of vertices
    arr = []
    
    # Reading the adjacency matrix
    for i in range(n):
        arr.append(list(map(int, input().split())))
    
    adjacency_list = [[] for _ in range(n)]
    
    # Convert adjacency matrix to adjacency list
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: 
                adjacency_list[i].append(j + 1)  # Append j+1 (1-based indexing)
    
    # Print the adjacency list in the desired format
    for i in range(n):
        # Print vertex number followed by its neighbors
        print(len(adjacency_list[i]), *sorted(adjacency_list[i]))
