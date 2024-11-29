# unweighted graph 
def create_adjacency_matrix(vertices, edges):
    n = len(vertices)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Add edges
    for u, v in edges:
        adjacency_matrix[u-1][v-1] = 1  # Mark edge u -> v
        adjacency_matrix[v-1][u-1] = 1  # For undirected graphs, mark edge v -> u as well
    
    return adjacency_matrix

# Example usage
vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]

adj_matrix = create_adjacency_matrix(vertices, edges)
for row in adj_matrix:
    print(row)
    
    
# weighted graph    
def create_weighted_adjacency_matrix(vertices, edges, weights):
    n = len(vertices)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for (u, v), weight in zip(edges, weights):
        adjacency_matrix[u-1][v-1] = weight
        adjacency_matrix[v-1][u-1] = weight  # For undirected graphs
    
    return adjacency_matrix

vertices = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
weights = [5, 3, 2, 4]

adj_matrix = create_weighted_adjacency_matrix(vertices, edges, weights)
for row in adj_matrix:
    print(row)
 
