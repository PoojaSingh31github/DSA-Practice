# undirected graph

def create_adjacency_list(vertices, edges):
    # Initialize the adjacency list
    adjacency_list = {vertex: [] for vertex in vertices}
    
    # Add edges
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)  # Add this line only if the graph is undirected
    
    return adjacency_list



vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (3, 4), (4, 5)]

adj_list = create_adjacency_list(vertices, edges)
print(adj_list)


# directed graph
def create_directed_adjacency_list(vertices, edges):
    adjacency_list = {vertex: [] for vertex in vertices}
    for u, v in edges:
        adjacency_list[u].append(v)  # Only add the directed edge u -> v
    return adjacency_list

vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (3, 4), (4, 5)]

adj_list = create_directed_adjacency_list(vertices, edges)
print(adj_list)
