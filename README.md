
NAMES: NIYIGENA Djamila
Reg Number:223017067
Project Number:75

GRAPH USING ADJACENCY LIST
This project is about building and managing graphs using C++. A graph is made up of points (called vertices) connected by lines (called edges).
We use an adjacency list to store the graph each vertex keeps a list of the other vertices it’s connected to.
The project supports two types of graphs:
•	Directed Graph: Connections go in one direction.
•	Unweighted Graph: Connections go both ways and all edges have the same weight.
The code uses classes and inheritance to handle both graph types in a clean, reusable way. It also uses dynamic memory and pointer arithmetic to manage memory efficiently
#include <iostream>   // For input/output operations (cout, endl)
#include <cstring>    // For memcpy (not used here but included)
using namespace std;  // Use the std namespace to avoid writing std::
/* --- Struct Definitions --- */
// Defines an Edge connecting to a vertex with an associated weight
struct Edge {
    int to;          // ID of the vertex this edge points to
    float weight;    // Weight of the edge
};
// Defines a Vertex in the graph with dynamic edges
struct Vertex {
    int id;          // Vertex identifier
    Edge* edges;     // Dynamic array of edges (adjacency list)
    int edgeCount;   // Number of edges currently stored
    int edgeCapacity; // Current capacity of the edges array

    // Constructor to initialize members
    Vertex() : id(-1), edges(nullptr), edgeCount(0), edgeCapacity(0) {}
  // Adds an edge dynamically, resizing edges array if needed
    void addEdge(int to, float weight) {
        if (edgeCount == edgeCapacity) {
            // Double the capacity or start with 2 if empty
            edgeCapacity = edgeCapacity == 0 ? 2 : edgeCapacity * 2;
            Edge* newEdges = new Edge[edgeCapacity];
            // Copy existing edges using pointer arithmetic
            for (int i = 0; i < edgeCount; ++i)
                *(newEdges + i) = *(edges + i);
            delete[] edges;   // Delete old edges array
            edges = newEdges; // Point to new bigger array
        }
        // Insert new edge at the next free position using pointer arithmetic
        *(edges + edgeCount) = Edge{to, weight};
        ++edgeCount;  // Increase edge count
    }

    // Frees the memory used by edges and resets counts
    void freeEdges() {
        delete[] edges;
        edges = nullptr;
        edgeCount = 0;
        edgeCapacity = 0;
    }
};
/* --- Abstract Graph Interface --- */
// Abstract base class for graphs
class Graph {
protected:
    Vertex* vertices;    // Dynamic array of vertices
    int vertexCount;     // Number of vertices currently stored
    int vertexCapacity;  // Capacity of the vertices array

public:
    // Constructor initializes empty graph
    Graph() : vertices(nullptr), vertexCount(0), vertexCapacity(0) {}

    // Pure virtual function to add edges, must be implemented by derived classes
    virtual void addEdge(int from, int to, float weight) = 0;
// Destructor cleans up all allocated memory
    virtual ~Graph() {
        for (int i = 0; i < vertexCount; ++i)
            vertices[i].freeEdges();  // Free edges for each vertex
        delete[] vertices;            // Free vertices array
    }
  // Adds a vertex if it doesn't exist already
    void addVertex(int id) {
        if (findVertex(id) != -1) return; // Vertex already exists, do nothing
 // Resize vertices array if full
        if (vertexCount == vertexCapacity) {
            vertexCapacity = vertexCapacity == 0 ? 2 : vertexCapacity * 2;
            Vertex* newVertices = new Vertex[vertexCapacity];
            // Copy old vertices
            for (int i = 0; i < vertexCount; ++i)
                newVertices[i] = vertices[i];
            delete[] vertices;     // Delete old array
            vertices = newVertices; // Point to new bigger array
        }
 vertices[vertexCount].id = id; // Set new vertex ID
        ++vertexCount;                 // Increment count
    }
   // Removes vertex with the given ID
    void removeVertex(int id) {
        int index = findVertex(id);  // Find vertex index
        if (index == -1) return;     // Vertex not found, do nothing
 vertices[index].freeEdges(); // Free memory used by edges of this vertex
        // Shift vertices down to fill the removed spot
        for (int i = index; i < vertexCount - 1; ++i)
            vertices[i] = vertices[i + 1];
        --vertexCount; // Reduce count
    }
 // Finds the index of a vertex by id, or -1 if not found
    int findVertex(int id) const {
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id)
                return i;
        return -1;
    }
    // Returns pointer to vertex by id, or nullptr if not found
    Vertex* getVertex(int id) {
        int idx = findVertex(id);
        return (idx != -1) ? &vertices[idx] : nullptr;
    }
// Prints all vertices and their edges
    void printGraph() {
        for (int i = 0; i < vertexCount; ++i) {
            cout << "Vertex " << vertices[i].id << ": ";
            for (int j = 0; j < vertices[i].edgeCount; ++j) {
                Edge* e = vertices[i].edges + j;  // Pointer arithmetic
                cout << "(" << e->to << ", " << e->weight << ") ";
            }
            cout << endl;
        }
    }
};
/* --- DirectedGraph Implementation --- */
// Derived class implementing a directed graph
class DirectedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight) override {
        addVertex(from);  // Ensure vertices exist
        addVertex(to);
        getVertex(from)->addEdge(to, weight);  // Add directed edge
    }
};
/* --- UnweightedGraph Implementation --- */
// Derived class implementing an unweighted, undirected graph
class UnweightedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight = 1.0f) override {
        addVertex(from);  // Ensure vertices exist
        addVertex(to);
        getVertex(from)->addEdge(to, 1.0f);  // Add edge from from->to with weight=1
        getVertex(to)->addEdge(from, 1.0f);  // Add edge from to->from to make undirected
    }
};
/* --- Usage Example --- */
int main() {
    int graphCount = 2;
    graphs = new Graph [graphCount];  // Dynamic array of graph pointers
    graphs[0] = new DirectedGraph();   // Create directed graph
    graphs[1] = new UnweightedGraph(); // Create unweighted undirected graph

    // Add edges to directed graph
    graphs[0]->addEdge(1, 2, 5.0f);
    graphs[0]->addEdge(1, 3, 2.0f);
    graphs[0]->addEdge(2, 4, 3.0f);

    // Add edges to unweighted graph (undirected)
    graphs[1]->addEdge(10, 20, 1.0f);
    graphs[1]->addEdge(10, 30, 1.0f);
    graphs[1]->addEdge(20, 40, 1.0f);

    // Print graphs
    cout << "Directed Graph:\n";
    graphs[0]->printGraph();
cout << "\nUnweighted Graph:\n";
    graphs[1]->printGraph();

    // Clean up dynamic memory
    for (int i = 0; i < graphCount; ++i)
        delete graphs[i];
    delete[] graphs;
    return 0;
}
This project demonstrates how to build and manage graphs using adjacency lists in C++. It uses dynamic arrays and pointer arithmetic to store edges efficiently.
By creating a common Graph interface and extending it with DirectedGraph and UnweightedGraph, the project shows the power of object-oriented programming with inheritance and polymorphism.
It allows adding and removing vertices, adding edges, and printing graph connections, providing a flexible and memory-efficient way to work with different types of graphs.

