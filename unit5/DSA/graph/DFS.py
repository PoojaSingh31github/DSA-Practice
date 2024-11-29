def dfs(graph, node, visited):
    # Mark the current node as visited
    visited[node] = True
    print(node, end=" ")  # Visit the node (print or process it)
    
    # Visit all the unvisited neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)  # Recursively visit the neighbor

# Example usage:
# Graph represented as an adjacency list
# 0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Number of nodes
n = len(graph)

# Create a visited array to keep track of visited nodes
visited = [False] * n

# Starting node is 0
dfs(graph, 0, visited)
