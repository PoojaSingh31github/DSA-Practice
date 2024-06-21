class Graph {
  constructor(vertices) {
    this.vertices = vertices;
    this.adjList = new Map();

    // Initialize the adjacency list with empty arrays
    for (let i = 0; i < vertices; i++) {
      this.adjList.set(i, []);
    }
  }

  addEdge(v, w) {
    // Add an edge from v to w (undirected graph)
    this.adjList.get(v).push(w);
    this.adjList.get(w).push(v);
  }

  printGraph() {
    // Get all the vertices
    const keys = this.adjList.keys();

    // Iterate over the vertices
    for (let key of keys) {
      const values = this.adjList.get(key);
      let adjVertices = "";

      // Iterate over the adjacency list of a vertex and concatenate the values into a string
      for (let value of values) {
        adjVertices += value + " ";
      }

      // Print the vertex and its adjacency list
      console.log(key + " -> " + adjVertices);
    }
  }
}

// Example usage for both 
const vertices = 4;
const edges = [
  [0, 1],
  [0, 2],
  [1, 2],
  [2, 3],
];

const graph = new Graph(vertices);

// Adding edges to the graph
for (let edge of edges) {
  graph.addEdge(edge[0], edge[1]);
}

// Print the adjacency list
graph.printGraph1();


class Graph {
  constructor(vertices) {
    this.vertices = vertices;

    // Initialize the adjacency matrix with 0s
    this.adjMatrix = Array.from({ length: vertices }, () =>
      Array(vertices).fill(0)
    );
  }

  addEdge(v, w) {
    // Add an edge from v to w (undirected graph)
    this.adjMatrix[v][w] = 1;
    this.adjMatrix[w][v] = 1;
  }

  printGraph() {
    // Print the adjacency matrix
    for (let i = 0; i < this.vertices; i++) {
      let row = "";
      for (let j = 0; j < this.vertices; j++) {
        row += this.adjMatrix[i][j] + " ";
      }
      console.log(row);
    }
  }
}

// Adding edges to the graph
for (let edge of edges) {
  graph.addEdge(edge[0], edge[1]);
}

// Print the adjacency matrix
graph.printGraph();
