from collections import deque

def bfs(graph, start):
    # Create a unvisited array 
    visited = [False] * len(graph)
    
    # Create a queue 
    queue = deque()
    
    # Start with the source node
    visited[start] = True
    queue.append(start)
    
    # Process the nodes in the queue
    while queue:
        node = queue.popleft()  # Dequeue the element
        print(node, end=" ")    # Visit the node (print or process it)
        
        # Visit all the neighbors of the current node
        print(graph[node])
        for neighbor in graph[node]:
            if not visited[neighbor]:  # If neighbor hasn't been visited yet
                visited[neighbor] = True
                queue.append(neighbor)  # Enqueue the neighbor

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

# Starting node is 0
bfs(graph, 0)
